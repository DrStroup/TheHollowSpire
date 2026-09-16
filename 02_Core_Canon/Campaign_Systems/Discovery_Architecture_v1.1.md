# Discovery Architecture

Status: Current clarification, 2026-09-16.
Sources: [Codex/Hunts integration](Codex_Hunts_Integration.md), [Discovery Registry](Discovery_Registry_Framework_v1.0.md).

## Views of discoveries

1. Floor checklist: findings tied to zones.
2. Encounter checklist: findings arising from encounters.
3. Integrated Codex/Hunt record: observations, evidence, samples, and investigation progress.

These are views into shared findings, not independent pools of rewards. Hunt is an activity within the Codex system.

## Counting

Every awardable finding has one canonical award key. A finding appearing in multiple views contributes to Campaign Discovery Total once.

Use [Discovery aliases](../../07_Registries/Discovery_Aliases.json) for established equivalents. An archive object ID is not automatically a discovery award ID. Unmapped legacy records need review before they award points.

Campaign Discovery Total feeds the existing Discovery Threshold Framework. No threshold amounts are changed here.
