# Artifact Generation Sequence Rule v1.0

## Locked Rule

Every artifact asset must follow the same production sequence:

```text
Generate
→ Review
→ Revise
→ Review
→ Lock
→ Place in Homebrewery
→ Update Registry
```

## Requirements

No asset may skip directly from first generation to layout placement.

Each asset must receive:

- First-generation review
- Revision decision
- Registry update
- Placement audit after Homebrewery integration

## Status Terms

Allowed production statuses:

- Planned
- Generated
- Prototype Approved
- Revision Required
- Rejected
- Revised
- Locked for Layout
- Placed
- Retired

## Registry Requirement

The Artifact Library Registry must be updated whenever an asset changes status.
