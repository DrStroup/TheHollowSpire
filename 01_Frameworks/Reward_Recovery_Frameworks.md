# Reward and Recovery Frameworks

**Version:** v1.0  
**Status:** Active Framework  
**Supersedes:** Discovery Credit / Recovery Cache reward model  

## Purpose

This framework defines how rewards function in *The Hollow Spire* publication line.

The purpose of rewards is not to create a currency economy. Rewards should make the world feel deeper, make exploration matter, and give players new ways to engage with places, people, routes, creatures, mysteries, settlements, and their own characters.

## Core Rule

**Rewards should be meaningful, not merely monetary.**

A reward is considered meaningful when it does at least one of the following:

- Reveals new information.
- Opens a new route, area, contact, or quest giver.
- Improves a settlement, outpost, camp, or faction relationship.
- Provides a useful material, tool, relic, map, component, or supply.
- Teaches a character something they could not do before.
- Changes how future exploration works.
- Strengthens the party's relationship with the Explorer Guild or local communities.
- Advances a mystery, seal, journey, contract chain, or floor objective.

Currency may exist in the setting for ordinary life, trade, and realism, but it should rarely be the most exciting reward offered by a contract, encounter, or discovery.

## Deprecated Reward Terms

The following terms are deprecated and should not be used as active mechanical reward categories:

- Discovery Credit
- Discovery Credits
- Recovery Cache
- Recovery Caches
- Guild Marks

Older files using these terms should be updated during publication conversion.

## Supported Reward Categories

### 1. Discovery Rewards

Discovery rewards are information-based rewards. They may reveal:

- Hidden rooms
- Forgotten names
- Old expedition routes
- Map corrections
- Lost history
- Seal clues
- Warden Ledger echoes
- Lantern lore
- Settlement secrets
- Contract leads
- Floor-to-floor connections

Discovery rewards are especially useful when the reward should change what the players understand rather than what they own.

### 2. Material Rewards

Material rewards are physical items recovered from the environment, ruins, creatures, or settlements.

Examples:

- Iron Rat Whiskers
- Iron Rat Teeth
- Glowcap Spores
- Lantern Moss
- Cave Eel Teeth
- Deepwater Shell Fragments
- Ember Beetle Carapaces
- Salvaged copper wire
- Old prison keys
- Moon-silver dust
- Preserved expedition wax

Material rewards should have practical uses whenever possible, such as crafting, barter, ritual preparation, training requirements, equipment repair, lantern maintenance, settlement restoration, or contract completion.

### 3. Monster-Part Rewards

Monster-part rewards support the ecology of the Hollow Spire. Creatures should feel like part of a living environment, not only obstacles.

A creature entry may include:

- Harvestable parts
- Safe harvesting requirements
- Local uses
- Contract demand
- Crafting or training use
- Settlement value
- Risks of mishandling the material

Example:

**Iron Rat Whiskers** may be requested by a lanternwright because they conduct faint vibrations through stone and can be used to repair delicate tremor-sense instruments.

### 4. Training Rewards

Training rewards represent what explorers learn from surviving the Spire and helping its people.

Training rewards may include:

- A new maneuver
- A bonus proficiency or tool familiarity
- An extra use of an existing class ability
- A small maximum hit point increase
- A special exploration technique
- A settlement-taught survival method
- A faction-specific field practice
- A unique ability not found in the reference ruleset

Training rewards should be earned through story, mentorship, hardship, practice, or repeated contribution. They should not be handed out casually.

Publication-facing text should describe training in system-neutral language first. Mechanical implementation can be placed in GM guidance or internal conversion notes.

### 5. Access Rewards

Access rewards open people, places, services, and opportunities.

Examples:

- Permission to enter a restricted passage
- Access to a quest giver
- A settlement elder agrees to speak with the party
- A ferryman opens a route
- The guild grants map-room access
- A sealed workroom becomes available
- A hidden outpost is restored
- A local guide agrees to travel with the party

Access rewards are often stronger than money because they change the campaign map.

### 6. Route and Travel Rewards

Route rewards improve movement through the Hollow Spire.

Examples:

- Faster travel routes
- Safer camps
- Repaired bridges
- Restored lantern outposts
- New waystations
- Marked descent paths
- Ferry crossings
- Shortcut tunnels
- Stable rope routes
- Cleared hazards

These rewards reinforce the core campaign loop: explore, restore, return, and descend farther.

### 7. Settlement Rewards

Settlement rewards improve the world because the party acted.

Examples:

- A village gains safe water.
- A trade path reopens.
- A healer returns to service.
- A lantern post is lit again.
- A lost family is reunited.
- A workshop resumes production.
- A lookout tower is repaired.
- A camp becomes a permanent refuge.

Settlement rewards should be tracked because they express one of the central Hollow Spire themes: leave the world better than it was found.

### 8. Equipment and Tool Rewards

Equipment rewards should favor exploration tools over simple wealth.

Examples:

- Lantern upgrades
- Climbing gear
- Waterproof map cases
- Repair kits
- Expedition packs
- Signal whistles
- Special chalk
- Breathing reeds
- Surveyor's cord
- Guild field tools
- Temporary equipment loans

Equipment may be permanent, consumable, loaned, repaired, or unlocked through trust.

### 9. Social and Reputation Rewards

Social rewards change how people respond to the party.

Examples:

- Trusted explorer status
- Introductions to specialists
- Safer reception in settlements
- New contract offers
- Local witnesses become willing to speak
- Guides offer reduced risk routes
- A family, guild cell, or outpost publicly vouches for the party

Avoid reducing reputation to a currency-like point system unless a later framework explicitly requires it.

### 10. Narrative Progression Rewards

Some rewards are story movement.

Examples:

- A seal clue is confirmed.
- The Moon Lantern reacts.
- A Warden Ledger entry becomes legible.
- A hidden name is recovered.
- A floor mystery advances.
- A contract chain opens.
- A settlement's next crisis becomes visible.

These rewards should be presented clearly so the GM understands why the event matters.

## Reward Design Checklist

When designing or auditing a reward, ask:

1. Does this reward do more than add money?
2. Does it connect to a place, person, creature, route, mystery, or settlement?
3. Does it support exploration, restoration, survival, or discovery?
4. Could it unlock a future scene, contact, route, or ability?
5. Does it make the Spire feel more alive?
6. Does it avoid Guild Marks and other currency-like progression systems?
7. Is the reward publication-safe and system-neutral in its wording?

## Encounter Reward Format

Publication encounter files should use this structure:

```markdown
## Rewards and Outcomes

### Discoveries

### Materials and Recoveries

### Training or Techniques

### Access, Routes, or Contacts

### Settlement or Narrative Effects
```

Sections may be omitted when not applicable.

## Bestiary Reward Format

Creature files may include:

```markdown
## Harvests and Uses

### Common Recoveries

### Rare Recoveries

### Local Uses

### Contract Hooks

### Training Hooks
```

This format is optional until the bestiary publication pass, but it is the preferred direction.

## Audit Note

Any active file still using Discovery Credits, Recovery Caches, or Guild Marks should be flagged during publication audit and revised during the relevant conversion pass.
