# The Hollow Spire — Book 01 Publication Audit v1.1

Status: AUDIT COMPLETE — NO NEW MANUSCRIPT DRAFTING PERFORMED
Date: 2026-06-08
Scope: Repository inventory, manuscript audit, Homebrewery audit, canon audit, terminology scan, reward-framework scan, and publication-readiness assessment.

## 1. Executive Summary

Book 01 is structurally viable, but it is not yet publication-ready. The strongest assets are the locked front matter, Region 001 canon, Chapter 0 outline structure, and established Homebrewery scaffolding. The main blockers are legacy reward terminology, outdated Chapter 0 naming, older Floor 1-10/Floor 2-10 references, and incomplete publication manuscripts beyond the early material.

No new Chapter 0 manuscript content should be drafted until the conflict items below are resolved or explicitly accepted as archive-only.

## 2. Locked Authorities

| Authority | Status | Action |
|---|---:|---|
| Front Matter order and visual export | Locked | Preserve |
| Chapter 0 title: The Explorer Guild Primer | Locked | Update older references |
| Book 01 scope: Floors 1-12 | Locked | Replace older Floor 1-10 / 2-10 language |
| Region 001 floor progression | Locked | Preserve |
| Emberlight Village before Blackwater Run | Locked | Preserve |
| Blackwater Run as horror evacuation sequence | Locked | Preserve |
| Lantern Village as primary Book 01 hub | Locked | Preserve |
| Moon Lantern acquired around Floor 10 | Locked | Preserve |
| First Seal = Truth, acquired on Floor 12 | Locked | Preserve |
| System-neutral publication language | Locked | Apply to all public-facing text |
| Guild Marks removed from canon | Locked | Remove as reward/currency subsystem |
| Meaningful Reward Philosophy | Locked | Replace narrow discovery-only reward language |

## 3. Repository Inventory

| Area | Finding | Status | Action |
|---|---|---:|---|
| `00_Project_Status` | Contains old Floor 1-10 references. | Outdated | Update or mark superseded. |
| `01_Frameworks` | Contains both current and obsolete framework language. | Mixed | Reconcile reward and encounter frameworks. |
| `02_Core_Canon` | Region 001 canon is strong and mostly current. | Mostly Complete | Lock, with minor terminology pass. |
| `03_Maps` | Map assets exist; DM/player separation still needs review. | Partial | Audit later during art/map pass. |
| `04_Bestiary` | Four early creatures exist. | Partial | Add materials/drops/use hooks later. |
| `05_NPCs` | Nib exists. | Partial | Expand later. |
| `06_Encounters` | Floor 1 encounter files exist but use obsolete reward categories. | Partial / Outdated | Update reward blocks. |
| `07_Registries` | Recovery/discovery registries exist. | Partial | Reconcile with Meaningful Reward Philosophy. |
| `08_Art_Registry` | Strong art registry foundation. | Partial | Later visual audit. |
| `09_Homebrewery` | Strong scaffolding, but mixed old/new Chapter 0 language. | Partial / Mixed | Reconcile before Chapter 0 drafting. |
| `13_Audits` | Multiple useful audits exist; main audit rules need v1.1. | Partial | Keep expanding. |

## 4. Manuscript Audit

| Manuscript / Source | Status | Action |
|---|---:|---|
| `09_Homebrewery/Book_01/Chapter_00/Chapter_00_Outline_v2.0.md` | Complete outline | Lock as structure. |
| `09_Homebrewery/Book_01/Chapter_00/Chapter_00_Manuscript_v2.0.md` | Outline lock only | Use as Chapter 0 planning source. |
| `09_Homebrewery/Book_01/Chapter_00/Chapter_00_Manuscript_v1.0.md` | Partial / outdated title | Mine useful prose; do not use title. |
| `09_Homebrewery/Book_01/Chapter_00/Archive/Chapter_00_Full_Manuscript_Draft_v1.0.txt` | Archive / partial | Reference only; contains old “Dungeon Master” language. |
| `09_Homebrewery/Book_01/Book_01_Homebrewery_Source_v1.1.md` | Assembly scaffold | Update Chapter 0 title and source insert reference. |
| `09_Homebrewery/Book_01/Table_Of_Contents_v1.1.md` | Outdated | Update Chapter 0 title, Appendix E wording, and floor count if needed. |
| `09_Homebrewery/Book_01/Book_01_Publication_Audit.md` | Outdated | Supersede with this audit. |
| `06_Encounters/*.md` | Partial | Update obsolete reward categories. |
| `09_Homebrewery/Book_01/Encounter_Conversions/*.md` | Partial template | Replace Discovery Credit headings with Meaningful Rewards. |

## 5. Canon Audit

| Canon Element | Status | Notes | Action |
|---|---:|---|---|
| Explorer Guild | Complete | Central publication identity. | Lock. |
| Seven Seals | Complete | First Seal = Truth. | Lock. |
| Moon Lantern | Complete | Acquired around Floor 10. | Lock. |
| Cycle of Recurrence | Complete | Campaign-level canon. | Lock GM-facing. |
| Warden Ledger | Complete | Should remain GM-facing unless intentionally revealed. | Lock GM-facing. |
| Emberlight Village | Complete | Must occur before Blackwater Run. | Lock. |
| Blackwater Run | Complete | Horror evacuation sequence, not simple combat arc. | Lock. |
| Lantern Village | Complete | Major hub after Blackwater Run. | Lock. |
| Book 01 Floors 1-12 | Complete | Supersedes older Floors 1-10 language. | Lock. |
| Region 001 progression | Complete | Prison Cells -> Emberlight -> Blackwater Run -> Lantern Village -> Floors 4-12. | Lock. |

## 6. Terminology Scan Results

Text files were scanned excluding `.git` and historical export packages.

| Term / Pattern | Hits | Files | Status | Action |
|---|---:|---:|---|---|
| Guild Marks | 13 | 7 | Mostly valid as deprecation references, but must not appear as an active subsystem. | Review each usage. |
| Discovery Credit | 15 | 14 | Outdated as a narrow reward category. | Replace in active encounter and conversion files. |
| Recovery Cache | 6 | 4 | Too narrow if used as primary reward structure. | Replace or broaden. |
| Pathfinder | 1 | 1 | Appears in audit rule only. | Acceptable if in audit context. |
| D&D / proprietary named ruleset | 1 | 1 | Appears in audit rule only. | Acceptable if in audit context, avoid in publication text. |
| DM / Dungeon Master | 21 | 12 | Needs review; may be acceptable in internal maps/audits, but publication should prefer neutral language. | Replace in public-facing text with “GM” or “Guide” only if desired; otherwise keep in internal files. |
| Game Master | 2 | 2 | Generic, acceptable. | Keep. |
| Floor 1-10 / Floor 2-10 | 8 | 7 | Outdated scope language. | Replace with Floors 1-12 or mark superseded. |
| Running The Hollow Spire / Running the Spire | 13 | 11 | Outdated Chapter 0 title. | Replace public-facing Chapter 0 title with “The Explorer Guild Primer.” |
| gold / gp | 0 | 0 | No text issue found. | No action. |

## 7. Critical Conflicts

### Conflict 001 — Reward Framework

File: `01_Frameworks/Reward_Recovery_Frameworks.md`

Status: Outdated.

Issue: The file states that only two exploration reward categories exist: Discovery Credit and Recovery Cache. This conflicts with the locked Meaningful Reward Philosophy.

Required action: Rewrite as a broad reward framework supporting discovery, monster materials, training, special abilities, equipment, routes, social access, quest-givers, settlement services, and narrative progress.

### Conflict 002 — Encounter Framework

File: `01_Frameworks/Encounter_Framework_v0.02.md`

Status: Partial / outdated.

Issue: It still lists Recovery Caches and frames rewards in a narrower discovery/recovery model.

Required action: Update the Reward Audit Rule to include Meaningful Rewards and monster/material/training access categories.

### Conflict 003 — Encounter Reward Blocks

Files:
- `06_Encounters/EN-001_Awakening_in_the_Black_Cells.md`
- `06_Encounters/EN-004_Iron_Rat_Colony.md`
- `06_Encounters/EN-006_Silent_Jailer_Sighting.md`
- `06_Encounters/EN-007_Lost_Child_Event.md`
- `06_Encounters/EN-008_The_Breach_Crossing.md`

Status: Outdated reward language.

Issue: These use Discovery Credits and/or Recovery Caches.

Required action: Replace with concrete meaningful rewards. Example: Iron Rat Colony should include Iron Rat Whiskers or other material rewards.

### Conflict 004 — Encounter Conversion Templates

Files:
- `09_Homebrewery/Book_01/Encounter_Conversions/EN-001_Publication_Conversion.md`
- `EN-002_Publication_Conversion.md`
- `EN-003_Publication_Conversion.md`
- `EN-004_Publication_Conversion.md`
- `EN-005_Publication_Conversion.md`
- `EN-006_Publication_Conversion.md`
- `EN-007_Publication_Conversion.md`
- `EN-008_Publication_Conversion.md`

Status: Outdated template headings.

Issue: Each uses “Discovery Credits” under Rewards.

Required action: Replace with a Meaningful Rewards block:
- Discovery
- Materials / Recoveries
- Training / Capability
- Access / Route
- Settlement / Social
- Narrative Follow-Up

### Conflict 005 — Chapter 0 Title Drift

Status: Mixed.

Issue: Several files still call Chapter 0 “Running The Hollow Spire.” Current locked title is “The Explorer Guild Primer.”

Required action: Update public-facing Homebrewery and TOC files. Archive files can remain but should be marked superseded.

### Conflict 006 — Book Scope Drift

Status: Mixed.

Issue: Several project-status and audit files still refer to Book 01 covering Floors 1-10 or Floors 2-10. Current locked scope is Floors 1-12.

Required action: Update active status files; archive older files if not worth editing.

## 8. Missing Manuscript Inventory

| Missing / Partial Manuscript | Priority | Notes |
|---|---:|---|
| Chapter 0 full publication manuscript | Immediate | Must follow locked outline. |
| Chapter 0 Homebrewery-ready source | Immediate | Requires title and reward framework reconciliation first. |
| Meaningful reward framework examples | Immediate | Needed before contract examples. |
| Contract example with non-currency rewards | Immediate | Should include material/access/training reward, not Guild Marks. |
| Floor 1 publication prose | High | Existing encounter/canon files are not a finished chapter. |
| Region 001 overview chapter prose | High | Canon exists; prose likely missing. |
| Floors 2-12 publication manuscripts | Later | Major future work. |
| Bestiary material/drop hooks | Later | Should be added before final Book 01 bestiary lock. |
| Final Table of Contents | Later | Placeholder acceptable until manuscript order is stable. |

## 9. Publication Readiness Assessment

| Area | Readiness | Status |
|---|---:|---|
| Front Matter | 100% | Locked |
| Canon Foundation | 95% | Locked with minor terminology cleanup |
| Region 001 Structure | 95% | Locked |
| System-Neutral Framework | 90% | Strong, but older v1.0 should be superseded |
| Reward Framework | 45% | Needs reconciliation |
| Chapter 0 Outline | 95% | Locked |
| Chapter 0 Manuscript | 40% | Partial |
| Homebrewery Assembly | 75% | Good scaffold, mixed old/new content |
| Encounter Conversion Files | 50% | Templates need reward updates |
| Floor 1 Encounter Content | 60% | Usable base, not publication complete |
| Bestiary | 55% | Needs material/reward hooks |
| Book 01 Overall | 30% | Strong foundation, incomplete manuscript |

## 10. Recommended Next Writing Target

Do not draft Chapter 0 yet.

Recommended next file-work target:
1. Update `01_Frameworks/Reward_Recovery_Frameworks.md`.
2. Update `01_Frameworks/Encounter_Framework_v0.02.md` reward audit language.
3. Update `09_Homebrewery/Book_01/Encounter_Conversions/*.md` reward headings.
4. Update `06_Encounters/*.md` reward blocks from Discovery Credits / Recovery Caches into concrete Meaningful Rewards.
5. Update public-facing Chapter 0 title references.

After those updates are complete, begin:

`09_Homebrewery/Book_01/Chapter_00/Chapter_00_Publication_Manuscript_v1.0.md`

First section target:

`0.1 Welcome to the Hollow Spire`

## 11. Audit Conclusion

The audit confirms that the repository is ready for a controlled reconciliation pass, not new prose. The next safest production step is to update the reward framework, encounter reward language, and Chapter 0 title references while preserving existing canon and front matter.
