# Page 9 Header Framework Update v1.6

## Root Cause

The v1.5 headers were physically alternating correctly, but the visible text was identical on every page. This made the spread appear unchanged even when recto and verso alignment differed.

## Fix

- Recto / odd pages now use the current chapter title:
  `Chapter 0 — The Explorer Guild Primer`
- Verso / even pages now use the book title:
  `Book I — The Blackwater Warrens`
- Existing left/right positioning is retained.
