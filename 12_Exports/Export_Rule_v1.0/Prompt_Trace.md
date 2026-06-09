# Prompt Trace — Export Rule v1.0

## Context

During Asset_004 production, an initial export was created as a standalone zip that did not follow the locked Hollow Spire repository structure.

The user identified the issue and provided the repository structure for reference.

## Decision

A permanent export workflow rule was established.

## Locked Rule

Every asset lock must generate:

1. Canon File  
   Lives in `02_Core_Canon/` if new canon was established.

2. Art Direction File  
   Lives in `08_Art_Registry/`.

3. Homebrewery Asset Files  
   Lives in `09_Homebrewery/Book_01/Assets/Asset_xxx/`.

4. Publication Placement File  
   Lives under the relevant page folder.

5. Export Package  
   Lives in `12_Exports/`.

6. Prompt Trace  
   Required for recovery and continuity.

## Rationale

This structure prevents orphan exports, preserves decision context, and supports continuation across future chats.
