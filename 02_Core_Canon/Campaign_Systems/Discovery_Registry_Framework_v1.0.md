# THE HOLLOW SPIRE

## Discovery Registry Framework v1.0

### Status

Locked Framework.

### Purpose

The Discovery Registry is the DM-facing checklist used to track what the party has discovered.

It supports:

- Discovery Thresholds.
- Contract availability.
- Hunt progression.
- Codex progression.
- Settlement trust.
- Route unlocks.
- Archive access.
- Hidden rewards.
- Campaign pacing.

Discovery is a hidden or semi-hidden system. Players should not normally see Discovery point values or threshold math.

### Core Principle

The campaign rewards discovery more than killing.

Discovery tracks meaningful engagement with the world.

### Discovery Entry Format

Each discovery should use the following format:

```text
D-###  [ ]  Discovery Name
Zone:
Category:
Value:
Mandatory:
Player-Facing Summary:
DM Notes:
Follow-Up:
Related Systems:
```

### Required Fields

#### Discovery ID
A unique identifier.

Recommended format:

- D-001, D-002, D-003 for campaign-wide use.
- F001-D001 for floor-specific use when needed.

#### Checklist Box
The DM should be able to mark the discovery as found.

Example:

```text
F001-D001  [ ]  The Prison No Longer Functions
```

#### Discovery Name
Short, readable, and easy to reference.

#### Zone
The zone where the discovery occurs.

Example:

Zone 01 — Black Cells.

#### Category
Use one primary category.

Allowed categories:

- Story
- Environmental
- Historical
- Exploration
- Codex
- Hunt
- Settlement
- Contradiction
- Route
- Wonder
- Resource
- Warden

#### Value
Discovery point value.

Suggested scale:

- 1 point: Minor discovery.
- 2–3 points: Useful discovery.
- 5 points: Major discovery.
- 10+ points: Region-shaping discovery.
- Custom: Book-level discovery.

#### Mandatory
Yes or No.

Mandatory means the discovery is expected for progression.

Optional means it rewards exploration but is not required.

#### Player-Facing Summary
What the players understand.

This should avoid protected canon unless the players are meant to know it.

#### DM Notes
What the discovery really means.

This may include protected canon.

#### Follow-Up
What discovery, route, quest, or clue this points toward.

#### Related Systems
Examples:

- Codex
- Hunt
- Contract
- Lantern Stability
- Settlement
- Warden Question
- Archive
- Route Unlock
- Companion Chip

---

## Floor Tally Section

Every floor discovery checklist should include a tally section at the bottom.

Example:

```text
FLOOR 001 DISCOVERY TALLY

Story Discovery:          _____ / _____
Environmental Discovery:  _____ / _____
Historical Discovery:     _____ / _____
Exploration Discovery:    _____ / _____
Codex Discovery:          _____ / _____
Hunt Discovery:           _____ / _____
Settlement Discovery:     _____ / _____
Contradiction Discovery:  _____ / _____
Route Discovery:          _____ / _____
Wonder Discovery:         _____ / _____
Resource Discovery:       _____ / _____
Warden Discovery:         _____ / _____

Floor Discovery Earned:   _____
Floor Discovery Available:_____
Campaign Discovery Total: _____

Hidden Thresholds Crossed:
[ ] 25 Discovery
[ ] 50 Discovery
[ ] 100 Discovery
[ ] 200 Discovery
[ ] Custom: __________________
```

---

## Floor 001 Starter Checklist

This is an initial implementation example for Floor 001.

```text
F001-D001  [ ]  The Prison No Longer Functions
Zone: Zone 01 — Black Cells
Category: Story
Value: 3
Mandatory: Yes
Player-Facing Summary: The prison no longer appears capable of holding prisoners.
DM Notes: Establishes the opening theme without revealing Recurrence.
Follow-Up: Rotunda; Nib; Lantern Stability.
Related Systems: Warden Question, Floor Theme

F001-D002  [ ]  Explorer Map #17 Contradiction
Zone: Zone 01 — Black Cells
Category: Contradiction
Value: 2
Mandatory: No
Player-Facing Summary: The explorer map does not perfectly match the current layout.
DM Notes: First contradiction. Should appear explainable as an outdated or inaccurate map.
Follow-Up: Future map contradictions.
Related Systems: Explorer Maps, Warden Question

F001-D003  [ ]  Missing Explorer Evidence
Zone: Zone 01 — Black Cells
Category: Historical
Value: 1
Mandatory: No
Player-Facing Summary: An explorer appears to have used one cell as shelter, but no body remains.
DM Notes: Reinforces that others came before the party.
Follow-Up: Explorer records; hidden expedition traces.
Related Systems: Archive, Explorer Guild

F001-D004  [ ]  Iron Rats Explain Prison Decay
Zone: Zone 01 — Black Cells
Category: Environmental
Value: 1
Mandatory: No
Player-Facing Summary: Iron Rats gnaw metal and contribute to structural failure.
DM Notes: Teaches ecology and environmental causality.
Follow-Up: Iron Rat materials; creature materials.
Related Systems: Encounter, Loot, Codex

F001-D005  [ ]  First Sight of Nib
Zone: Zone 01 — Black Cells
Category: Story
Value: 2
Mandatory: Yes
Player-Facing Summary: A living figure moves in the Rotunda below.
DM Notes: Creates relief and transitions to Zone 02.
Follow-Up: Nib Introduction.
Related Systems: Social Encounter, Lantern Stability Tutorial
```

---

## Discovery Design Rules

### Do
- Reward curiosity.
- Reward observation.
- Reward route discovery.
- Reward meaningful interaction.
- Reward recovering records.
- Reward understanding environmental causes.
- Reward helping settlements.
- Reward resolving contradictions.

### Do Not
- Award Discovery for repetitive grinding.
- Reveal point values to players.
- Treat Discovery as currency.
- Use Discovery as a visible quest checklist.
- Confirm late-game canon too early.

### Presentation Rule

Avoid:

```text
+3 Discovery
```

Use:

```text
Your lantern steadies.
```

or:

```text
The attendant glances at your lantern and seems to reconsider.
```

Discovery is recorded by the DM and expressed by the world.
