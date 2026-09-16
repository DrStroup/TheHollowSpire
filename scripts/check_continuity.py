#!/usr/bin/env python3
"""Validate the managed continuity records; historical archives are out of scope."""
import argparse
import json
from pathlib import Path
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

INDEX = "00_Project_Status/canon_index.json"
VIEW = "00_Project_Status/CANON_INDEX.md"
ALLOWED = {"accepted", "provisional", "draft", "superseded", "archived"}

def render_index(index):
    lines = [
        "# Canon index", "",
        "Generated from [canon_index.json](canon_index.json). Edit the JSON, then run",
        "`python3 scripts/check_continuity.py --write-index`.", "",
        "Authority is scoped by topic. An accepted framework may contain examples or open",
        "details; its status does not make every example final. Unlisted files are not",
        "automatically superseded: inspect their provenance and register conflicts.", "",
        "| Topic | Governing source | Status | Audience | Scope |",
        "|---|---|---|---|---|",
    ]
    for topic in index["topics"]:
        rel = posixpath.relpath(topic["path"], "00_Project_Status")
        lines.append(f'| {topic["title"]} | [{topic["id"]}]({rel}) | {topic["status"]} | {topic["audience"]} | {topic["scope"]} |')
    lines += ["", "Use [decisions](DECISIONS.md) for provenance and [open issues](CONTINUITY_ISSUES.md)",
              "for unresolved conflicts. Archives and exports preserve evidence, not parallel authority.", ""]
    return "\n".join(lines)

def validate(root, tracked, write_index=False):
    errors = []
    def read(path):
        try:
            return (root / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {path}: {exc}")
            return ""
    try:
        index = json.loads(read(INDEX))
    except (ValueError, TypeError) as exc:
        return [f"Invalid index: {exc}"]
    def exists(path):
        if path not in tracked:
            errors.append(f"Missing registered path: {path}")
    exists(index["decision_log"])
    exists(index["issues"])
    decisions = read(index["decision_log"])
    decision_list = re.findall(r"^## ((?:DOC|CAN)-\d+) —", decisions, re.M)
    decision_ids = set(decision_list)
    if len(decision_ids) != len(decision_list):
        errors.append("Duplicate decision ID")
    seen = set()
    superseded = {x["path"] for x in index["superseded"]}
    for topic in index["topics"]:
        if topic["id"] in seen:
            errors.append(f'Duplicate topic ID: {topic["id"]}')
        seen.add(topic["id"])
        exists(topic["path"])
        if topic["status"] not in ALLOWED:
            errors.append(f'Invalid status: {topic["id"]}')
        if topic["decision"] not in decision_ids:
            errors.append(f'Unknown decision: {topic["decision"]}')
        if topic["path"] in superseded:
            errors.append(f'Authority points to superseded file: {topic["id"]}')
    for item in index["superseded"]:
        exists(item["path"])
        exists(item["replacement"])
        if item["replacement"] in superseded:
            errors.append(f'Supersession chain is not direct: {item["path"]}')
    expected = render_index(index)
    if write_index:
        (root / VIEW).write_text(expected, encoding="utf-8")
    elif read(VIEW) != expected:
        errors.append("CANON_INDEX.md is stale; run with --write-index")
    for path in index["managed_documents"]:
        exists(path)
        text = read(path)
        # Check file targets; fragments and external link reachability are outside scope.
        for raw in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
            target = urlsplit(raw)
            if target.scheme or target.netloc or not target.path:
                continue
            dest = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(target.path)))
            if dest not in tracked and not any(p.startswith(dest.rstrip("/") + "/") for p in tracked):
                errors.append(f"Broken link in {path}: {raw}")
    topics = {x["id"]: x for x in index["topics"]}
    floor_text = read(topics["region_001_floors"]["path"])
    numbers = [int(n) for n in re.findall(r"^(\d{2}) [^\n]+$", floor_text, re.M)]
    if numbers != list(range(1, 13)):
        errors.append("Region floor authority must contain Floors 01–12 exactly once, in order")
    seal_text = read(topics["seven_seals"]["path"])
    seals = re.findall(r"^\| Seal ([IVX]+) \| ([^|]+) \|$", seal_text, re.M)
    if [x[0] for x in seals] != ["I", "II", "III", "IV", "V", "VI", "VII"] or len({x[1].strip() for x in seals}) != 7:
        errors.append("Seven Seals authority must have seven distinct, ordered entries")
    aliases_path = "07_Registries/Discovery_Aliases.json"
    exists(aliases_path)
    try:
        awards = json.loads(read(aliases_path))["awards"]
        keys = [a["award_key"] for a in awards]
        if len(keys) != len(set(keys)):
            errors.append("Duplicate Discovery award key")
        scoped = [(a["scope"], alias) for a in awards for alias in [a["award_key"]] + a["aliases"]]
        if len(scoped) != len(set(scoped)):
            errors.append("Ambiguous scoped Discovery alias")
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid Discovery aliases: {exc}")
    source = read(topics["publication_source"]["path"])
    for asset in re.findall(r"https://raw\.githubusercontent\.com/DrStroup/TheHollowSpire/main/([^\s\"<>)}]+)", source):
        asset = unquote(urlsplit(asset).path)
        if asset not in tracked:
            errors.append(f"Publication references missing repository asset: {asset}")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--inventory-json", type=Path, help="Offline list of repository paths")
    parser.add_argument("--write-index", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.inventory_json:
        tracked = set(json.loads(args.inventory_json.read_text(encoding="utf-8")))
    else:
        result = subprocess.run(["git", "ls-files", "-z"], cwd=root, text=True, capture_output=True, check=True)
        tracked = set(result.stdout.split("\0")) - {""}
    errors = validate(root, tracked, args.write_index)
    if errors:
        print("\n".join("ERROR: " + error for error in errors))
        return 1
    print("PASS: managed authority, decisions, links, floor/seal structure, award keys, and source image paths.")
    print("Not checked: all legacy files, image rendering, external URLs, or narrative truth.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
