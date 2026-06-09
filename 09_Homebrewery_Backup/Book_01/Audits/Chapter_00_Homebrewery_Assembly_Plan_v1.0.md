# Chapter 00 Homebrewery Assembly Plan v1.0

## Objective

Convert Chapter 00: The Explorer Guild Primer from manuscript into Homebrewery-ready source while preserving the locked front matter and Chapter 00 splash sequence.

## Source Audit Findings

- The current Homebrewery code contains front matter through the Chapter 00 splash page only.
- The uploaded PDF contains 9 pages. Pages 1-7 render the front matter. Page 8 appears as a parchment page with a broken/missing image indicator. Page 9 is a blank parchment page.
- The Chapter 00 manuscript v1.1 exists in the repository and includes sections 0.1 through 0.8.

## Assembly Decisions

| Item | Decision |
|---|---|
| Front matter | Preserve current asset pages |
| Chapter 00 splash | Keep as full-page art asset, update to v1.1 816x1056 asset |
| Chapter body | Insert after splash page |
| Sidebars | Use `.guildSidebar` and `.contractSidebar` |
| Contract example | Keep in section 0.4 |
| Page breaks | Insert between major sections for initial layout control |
| Page numbering | Continue after splash page unless later print layout requires reset |

## Files Produced

- `Book_01_Homebrewery_Source_v1.2.md`
- `Source/Book_01_Homebrewery_Source_v1.2.md`
- `Chapter_00/Chapter_00_Homebrewery_Assembly_v1.0.md`
- `Manuscript/TXT/Chapter_00_Homebrewery_Assembly_v1.0_Development_Notes.txt`
- `Audits/Chapter_00_Homebrewery_Assembly_Audit_v1.0.md`

## Next Required Action

Paste `Book_01_Homebrewery_Source_v1.2.md` into Homebrewery, export a fresh PDF, and perform a visual layout audit.
