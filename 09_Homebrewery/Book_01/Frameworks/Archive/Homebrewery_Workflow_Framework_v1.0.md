# Hollow Spire Homebrewery Workflow Framework v1.0

## Status

Locked workflow rule for Homebrewery layout and publication passes.

## Purpose

This framework standardizes how Homebrewery code changes are provided, tested, audited, and exported during publication development of The Hollow Spire.

---

## Core Rule

When modifying a Homebrewery page, provide the complete replacement page block.

Do not provide fragment-only code unless the user specifically requests a diff.

---

## Required Response Format for Homebrewery Page Changes

Every Homebrewery page update should include:

1. Full Page Replacement Block
   - The complete page block from opening wrapper to closing wrapper.
   - Includes all text, sidebars, art containers, and page-specific layout elements.
   - Safe for direct copy/paste.

2. Required CSS
   - Only include CSS that is new or changed.
   - Clearly state whether it should be added to the global style block, Chapter 0 style block, or page-specific style block.

3. Required Assets
   - Filename.
   - Repository path.
   - Raw GitHub URL if needed for Homebrewery.
   - Whether the asset must be pushed before testing.

4. Placement Notes
   - Page number.
   - Section number.
   - Intended visual purpose.
   - Expected position of art, sidebar, footer, and text.

5. Expected Render Result
   - What the PDF should look like after applying the change.
   - Known risks to check, such as overlap, overflow, image scale, footer conflict, or broken asset URL.

6. Audit Instruction
   - User exports a PDF after paste.
   - Assistant audits the rendered PDF before proceeding.

---

## Code Safety Rules

- Avoid partial snippets when full replacement blocks are practical.
- Do not assume the user can identify the exact insertion point from a fragment.
- Do not change manuscript content during layout polish unless explicitly approved.
- Do not overwrite locked front matter or splash pages unless an audit identifies a technical issue.
- Preserve canonical file paths.
- Preserve current repository structure.
- When adding assets, include a zip with files in correct repository locations.
- When adding Homebrewery code, provide both a reusable source file and direct paste code where useful.

---

## Art Placement Rules

For Chapter 0 supporting art:

- Use watercolor or masked art treatment where possible.
- Favor bottom, side, or corner art that supports text instead of competing with it.
- Preserve readability above visual density.
- Avoid art taking more than roughly 25–35% of a manuscript page unless the page is intentionally art-forward.
- Do not add art to locked full-page front matter unless explicitly approved.

---

## Footer Rules

Visible page numbers should eventually be implemented on manuscript pages.

Do not show footer/page numbers on:

- cover page
- blank reverse
- title page
- dedication page
- oath page
- credits page
- contents placeholder page
- full-page chapter splash pages

Footer implementation should use the Explorer Guild crest or simplified crest mark if technically feasible.

---

## Audit-First Rule

Before new writing, major layout restructuring, or broad code replacement:

1. Audit current manuscript.
2. Audit current Homebrewery code.
3. Audit current PDF render.
4. Identify conflicts or missing assets.
5. Only then provide new replacement code.

---

## Current Locked Application

This workflow is locked beginning with:

- Chapter 0 Page 09 Layout Polish v1.1
- Art 01 — The First Descent
- Footer/page-number implementation testing
