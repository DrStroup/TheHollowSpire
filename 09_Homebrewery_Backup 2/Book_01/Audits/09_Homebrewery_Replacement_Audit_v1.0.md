# 09_Homebrewery Replacement Audit v1.0

## Audited File

`09_Homebrewery_Chapter00_Assembled_v1.1_FULL.zip`

## Verdict

**PASS WITH CLEANUP REQUIRED BEFORE FULL REPLACEMENT**

The ZIP does contain the full `09_Homebrewery` directory and the assembled Chapter 0 v1.1 manuscript. However, because it preserves the previous folder contents, it also preserves several older audit/archive/source files that still contain deprecated terminology or outdated scope references.

This does not invalidate the Chapter 0 v1.1 manuscript, but it means the folder should not be treated as fully clean until legacy references are either updated, archived clearly, or marked superseded.

---

## Confirmed Present

### Required Folder

- `09_Homebrewery/`

### Required Chapter 0 Assembled Files

- `09_Homebrewery/Book_01/Manuscript/Chapter_00_Explorer_Guild_Primer_Publication_v1.1.md`
- `09_Homebrewery/Book_01/Manuscript/TXT/Chapter_00_Explorer_Guild_Primer_Publication_v1.1_Development_Notes.txt`
- `09_Homebrewery/Book_01/Audits/Chapter_00_Publication_Audit_v1.1.md`

### Existing Asset Structure Preserved

Confirmed preserved:

- `Book_01/Art/`
- `Book_01/Source/`
- `Book_01/Chapter_00/`
- `Book_01/Encounter_Conversions/`
- `Book_01/Manuscript/`

---

## Chapter 0 v1.1 Manuscript Audit

### Status

**PASS**

### Confirmed Sections

- 0.1 Welcome to the Hollow Spire
- 0.2 The Explorer Guild
- 0.3 Discovery
- 0.4 Contracts
- 0.5 Exploration & Danger
- 0.6 Horror & Wonder
- 0.7 Leave the World Better Than You Found It
- 0.8 Beginning the Journey

### Content Checks

| Check | Result |
|---|---|
| Complete section sequence | Pass |
| System-neutral publication language | Pass |
| No proprietary rules terminology in Chapter 0 v1.1 manuscript | Pass |
| No Guild Marks in Chapter 0 v1.1 manuscript | Pass |
| Reward philosophy alignment | Pass |
| Explorer Guild philosophy alignment | Pass |
| Transition to Blackwater Warrens | Pass |

---

## Cleanup Findings

The following terms were found somewhere in the replacement `09_Homebrewery` folder.

### Deprecated Guild Mark References

Found in:

- `Book_01/Book_01_Architecture_Recovery_v1.0.md`
- `Book_01/Book_01_Publication_Audit.md`
- `Book_01/Audits/Chapter_00_Publication_Audit_v1.1.md`
- `Book_01/Manuscript/TXT/Chapter_00_Explorer_Guild_Primer_Publication_v1.0_Development_Notes.txt`
- `Book_01/Manuscript/TXT/Chapter_00_Sections_05_06_Development_Notes.txt`
- `Book_01/Manuscript/TXT/Chapter_00_Explorer_Guild_Primer_Publication_v1.1_Development_Notes.txt`

Most of these are audit/development-note references saying “No Guild Marks,” which are acceptable. The file requiring cleanup is:

- `Book_01/Book_01_Architecture_Recovery_v1.0.md`

### Deprecated Discovery Credit / Recovery Cache References

Found in:

- `Book_01/Book_01_Publication_Audit.md`

This file appears to be an older audit document and should be superseded, updated, or moved into an archive.

### Deprecated Scope Reference

Found:

- `Book_01/Book_01_Architecture_Recovery_v1.0.md`

Issue:

- References `Floors 1–10`

Current canon:

- Book 01 covers `Floors 1–12`

Action:

- Update or mark superseded.

### Proprietary / System-Specific Reference

Found:

- `Book_01/Book_01_Homebrewery_Source.md`

Term detected:

- `Dungeons`

Action:

- Review context and replace if this is a public-facing phrase.
- If it is only generic “dungeons” as a common noun, no change is required.

---

## Recommended Fixes Before Proceeding

### High Priority

1. Update or supersede `Book_01/Book_01_Architecture_Recovery_v1.0.md`
   - Remove/update Guild Mark reference.
   - Update Floors 1–10 to Floors 1–12.

2. Update or archive `Book_01/Book_01_Publication_Audit.md`
   - Remove Discovery Credit / Recovery Cache references.
   - Replace with current reward philosophy language.

### Medium Priority

3. Review `Book_01/Book_01_Homebrewery_Source.md`
   - Confirm whether “Dungeons” is being used generically.
   - Replace if it is referencing a protected product name or system-specific framing.

4. Consider moving older Chapter 0 files to `Chapter_00/Archive/Deprecated/`
   - `Chapter_00_Manuscript_v1.0.md`
   - `Chapter_00_Manuscript_v2.0.md`
   - `Chapter_00_Outline_v2.0.md`

---

## Recommendation

Do **not** proceed to Floor 1 yet.

Next task should be:

**09_Homebrewery Cleanup Pass v1.2**

Goal:

- Preserve the complete replacement folder.
- Update or archive legacy files with outdated terminology.
- Keep Chapter 0 v1.1 as the authoritative manuscript.
- Export a clean replacement `09_Homebrewery` ZIP.

Once that cleanup is complete, Chapter 0 can be treated as safely assembled and ready for Homebrewery layout work.
