# Documentation continuity workflow

Status: Active process, authorized by the repository-correction request on 2026-09-16.

## Authority

GitHub preserves the record. The [canon index](../00_Project_Status/CANON_INDEX.md) identifies authority by topic and scope. A file's presence, date, version suffix, or isolated “locked” label is not sufficient to override an explicit decision.

Accepted: current approved direction. Provisional: working direction with named open details. Draft: not yet accepted. Superseded: replaced by a named source. Archived: historical evidence.

During migration, do not invent historical approval dates. Record whether provenance is a source document, an explicit current user decision, or a prior user correction available in conversation context.

## Before work

Read current state and open issues. Locate and read the indexed sources. Name the topic and dependent files being changed. Keep deliberately undecided details visible.

## During work

Distinguish:
- Established GM truth.
- In-world belief or rumor.
- Player knowledge and reveal conditions.
- Design questions that have no established answer.

Draft suggestions remain draft until accepted. Where sources conflict without a governing decision, register the conflict instead of blending them silently.

Each accepted decision records its date, source, affected files, rationale, and remaining dependents. Use an atomic Git commit where practical; its history supplies the implementation commit without embedding a self-referential commit hash.

## Done for a work packet

1. Changed content and dependent records agree, or unresolved dependents are listed.
2. Decision record and current state are updated.
3. The continuity checker passes.
4. The changelog identifies scope and limitations.
5. The branch/commit or requested export preserves the result.
6. The handoff names one next task.

Git history preserves ordinary revisions. Stable live paths are preferred for new documents. Historical exports and prompt traces are evidence, not parallel authorities. For publication snapshots and downloadable packages, retain the existing export requirements.

## Separate histories

World history records setting events. Session logs record a specific table's experience. Design decisions record authoring changes. Do not infer that a campaign event happened merely because an encounter was written.

## Validation boundaries

The checker validates registered paths, topic IDs, decision IDs, supersession targets, registered document links, indexed floor/seal values, and publication image paths. It does not validate every historical file, visual layout, external URL availability, or narrative truth.
