# Asset Isolation Rule v1.0

## Locked Rule

When generating artifact assets, generate only the artifact itself.

Artifact generation must not produce:

- Asset sheets
- Presentation boards
- Workflow diagrams
- Framework summaries
- Style guides
- Multi-asset overview images

## Production Requirement

The final generated image should be a standalone production asset ready for placement in:

```text
09_Homebrewery/
└── Book_01/
    └── Art/
        └── Chapter_00/
            └── Artifacts/
```

## Purpose

This prevents concept sheets or design documentation from being mistaken for usable Homebrewery art assets.
