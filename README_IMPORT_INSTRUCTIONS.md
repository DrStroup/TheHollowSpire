# Hollow Spire Campaign Skeleton v1.0 — Import Instructions

This package corrects the previous export structure by removing the extra `02_Core_Canon/00_Worldgen/` and `00_Meta/` paths.

## Add these files

1. Add:
   `02_Core_Canon/Campaign/Hollow_Spire_Campaign_Skeleton_v1.0.md`

2. Add:
   `02_Core_Canon/Campaign/Prompt_Traces/Hollow_Spire_Campaign_Skeleton_v1.0_prompt_chain.txt`

## Remove these files if you already imported the previous zip

1. Delete:
   `02_Core_Canon/00_Worldgen/Hollow_Spire_Worldgen_Skeleton_v1.0.md`

2. Delete:
   `00_Meta/Prompt_Chains/Hollow_Spire_Worldgen_Skeleton_v1.0_prompt_chain.txt`

3. Delete the empty folders if present:
   `02_Core_Canon/00_Worldgen/`
   `00_Meta/Prompt_Chains/`
   `00_Meta/`

## Rename/move mapping

Previous path:
`02_Core_Canon/00_Worldgen/Hollow_Spire_Worldgen_Skeleton_v1.0.md`

New path:
`02_Core_Canon/Campaign/Hollow_Spire_Campaign_Skeleton_v1.0.md`

Previous path:
`00_Meta/Prompt_Chains/Hollow_Spire_Worldgen_Skeleton_v1.0_prompt_chain.txt`

New path:
`02_Core_Canon/Campaign/Prompt_Traces/Hollow_Spire_Campaign_Skeleton_v1.0_prompt_chain.txt`

## Recommended git commands

```bash
# From repo root
mkdir -p 02_Core_Canon/Campaign/Prompt_Traces

# If previous zip was already imported, move/rename instead of duplicate-adding
git mv 02_Core_Canon/00_Worldgen/Hollow_Spire_Worldgen_Skeleton_v1.0.md \
  02_Core_Canon/Campaign/Hollow_Spire_Campaign_Skeleton_v1.0.md

git mv 00_Meta/Prompt_Chains/Hollow_Spire_Worldgen_Skeleton_v1.0_prompt_chain.txt \
  02_Core_Canon/Campaign/Prompt_Traces/Hollow_Spire_Campaign_Skeleton_v1.0_prompt_chain.txt

# Remove empty folders if your system left them behind
rmdir 02_Core_Canon/00_Worldgen 2>/dev/null || true
rmdir 00_Meta/Prompt_Chains 2>/dev/null || true
rmdir 00_Meta 2>/dev/null || true

git status
```

If you did not import the previous zip, simply unzip this package at the repository root and commit the two new files.
