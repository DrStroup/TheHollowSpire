
# Encounter Discovery Registry v1.0

## Purpose

Encounter Discoveries are discoveries generated through interaction with encounters.

They use a separate checklist view from Zone Discoveries, but may refer to the same awardable finding.

Zone Discoveries = static discoveries tied to locations.

Encounter Discoveries = dynamic discoveries tied to encounters.

## Entry Format

ED-###
Name
Encounter
Category
Value
Repeatable
Discovery Potential
First Discovery Reward
Notes

## Categories

- Environmental
- Fauna
- Historical
- Wonder
- Social
- Threat
- Route
- Codex
- Hunt

## Example Entries

ED-001
Iron Rats Explain Prison Decay
Encounter: Iron Rat Nest
Category: Environmental
Value: 1
Repeatable: No
Discovery Potential: Minor

Award Key: F001-D004
Related Record IDs: ED-001, F001-D004
Award only the first time the party understands Iron Rats contribute to prison deterioration, including an earlier award from a floor checklist.

ED-002
First Sighting of a Crystal Shrine
Encounter: Crystal Shrine
Category: Wonder
Value: 7
Repeatable: No
Discovery Potential: Major

Award when the party meaningfully studies or records the shrine.

ED-003
Lantern Eel Migration Pattern
Encounter: Lantern Eels
Category: Fauna
Value: 3
Repeatable: No
Discovery Potential: Moderate

## Tracking Rule

Encounter Discoveries feed into the Campaign Discovery Total and Discovery Threshold Framework.

They may have their own checklist, but shared award keys prevent duplicate credit across views. See [Discovery aliases](../../07_Registries/Discovery_Aliases.json).
