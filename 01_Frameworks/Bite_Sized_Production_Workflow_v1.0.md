# Hollow Spire Bite-Sized Production Workflow v1.0

## Purpose

This workflow defines how Hollow Spire development proceeds from this point forward.

The goals are to prevent content loss, reduce canon drift, and keep each work session small enough to finish, export, archive, and resume later.

## Core Rule

Every development task must be broken into a bite-sized chunk.

A chunk is complete only when it has been exported.

## Chunk Size Rules

A single chunk should usually produce one of the following:

- One framework document
- One canon skeleton
- One manuscript section
- One encounter
- One NPC entry
- One art brief set
- One audit document
- One registry update
- One chapter outline
- One PDF/session handoff package

Avoid combining multiple major deliverables in one chunk.

## Recommended Chunk Length

For manuscript work:

- 500-1,500 words per chunk
- One subsection at a time
- No full chapter drafts unless explicitly requested

For canon/framework work:

- One concept or structure per chunk

For registries:

- One registry category per chunk

## Required Export Rule

Every completed chunk must be exported before moving on.

Each export should include:

1. The deliverable document
2. A TXT prompt-trace explaining how the result was derived
3. A changelog
4. Repository-relative file paths
5. Optional manifest JSON when useful

## Prompt Trace Rule

Any time a manuscript, skeleton, chain, outline, canon document, or framework is created, include a TXT file named:

`PROMPT_TRACE_<Deliverable_Name>_vX.X.txt`

The prompt trace should explain:

- The immediate user request
- The canon assumptions used
- The source documents or recovered notes referenced
- The reasoning path at a high level
- Any unresolved questions
- The intended next step

## Chat Session Rule

New chats should be opened for major sections.

Recommended chat boundaries:

- Campaign framework
- Region One canon
- Chapter 0
- Chapter 1
- Floor 001 manuscript
- Floor 002 manuscript
- Lantern Village
- Moon Lantern Sanctuary
- GM-only mysteries

## PDF End-of-Chat Rule

At the end of a major chat or section, produce a PDF summary when possible containing:

- What was completed
- What canon was established
- What files were exported
- What remains unresolved
- The next recommended task

## Stop Conditions

Do not proceed to the next chunk until:

- The current chunk has a clear output
- The output is exported
- The prompt trace is included
- The user has a ZIP or PDF reference package when appropriate

## Recovery Mode Rule

When recovering old Hollow Spire material:

1. Prefer user-provided original notes.
2. Prefer repository files.
3. Use memory/context only as support.
4. Mark invented or newly proposed material clearly.
5. Do not silently merge speculative content into canon.

## Publication Mode Rule

When writing manuscript prose:

- Use established canon.
- Maintain Pathfinder 1e assumptions.
- Preserve the campaign pillars:
  - Exploration
  - Contribution
  - Legacy
- Preserve the guiding philosophy:
  - Leave things better than you found them.
- Maintain tone:
  - 67% Dark
  - 33% Hope
- Avoid introducing major new lore unless intentionally requested.
