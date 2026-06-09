# Export Rule v1.0

Status: CANON / WORKFLOW LOCKED

## Purpose

Every completed asset lock must produce a Git-ready export package that follows the live Hollow Spire repository structure.

This prevents orphan exports, incomplete handoffs, and asset locks that are difficult to recover or continue in a later chat.

## Required Files for Every Asset Lock

### 1. Canon File

Required when new canon was established or modified.

Placement:
`02_Core_Canon/`

Purpose:
- Preserve newly locked setting, campaign, faction, law, rule, or lore canon.
- Keep canon separate from publication layout and art-direction files.

### 2. Art Direction File

Required when the asset includes visual design, image generation, style rules, or publication art requirements.

Placement:
`08_Art_Registry/`

Purpose:
- Preserve the approved visual treatment.
- Record thumbnail/readability requirements.
- Record recurring visual motifs and asset-specific style notes.

### 3. Homebrewery Asset Files

Required for every publication-facing asset.

Placement:
`09_Homebrewery/Book_01/Assets/Asset_xxx/`

Purpose:
- Store asset-facing copy, generation prompts, placement notes, and implementation-ready material.
- Keep all files for the specific asset together.

### 4. Publication Placement File

Required when the asset has a known page, spread, chapter, or layout role.

Placement:
Relevant page or publication folder under:
`09_Homebrewery/Book_01/Publication/`

Purpose:
- Record where the asset belongs.
- Record page role, layout assumptions, and production notes.

### 5. Export Package

Required for every lock package.

Placement:
`12_Exports/`

Purpose:
- Preserve a commit-ready bundle.
- Provide a readable handoff folder.
- Include README, changelog, and prompt trace.

### 6. Prompt Trace

Required for every asset lock.

Placement:
Inside the relevant export package under:
`12_Exports/`

Purpose:
- Preserve how the locked result was reached.
- Support continuity if future chats lose context.
- Record major decisions, rejected alternatives, and final lock rationale.

## Standard Asset Export Checklist

Before providing a zip, confirm the export includes:

- [ ] Canon file if canon changed.
- [ ] Art direction file if visuals changed or were established.
- [ ] Homebrewery asset folder.
- [ ] Publication placement file if a page/location is known.
- [ ] Export package folder.
- [ ] Prompt trace.
- [ ] Changelog.
- [ ] README.
- [ ] Git-ready folder structure.

## Locked Rule

Every asset lock must generate a repository-structured export package.

Do not provide standalone orphan files unless the user explicitly asks for a loose working draft.

## Status

LOCKED
