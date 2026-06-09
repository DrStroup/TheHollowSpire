# Chapter 00 Homebrewery Assembly Audit v1.0

## Verdict

**ASSEMBLY READY FOR HOMEBREWERY RENDER TEST**

This pass assembles the locked Chapter 00 manuscript into Homebrewery source. It should now be tested by pasting/exporting through Homebrewery and reviewing the resulting PDF.

## Inputs Reviewed

- `Homebrewery Code for The Hollow Spire.txt`
- `- The Hollow Spire - The Homebrewery.pdf`
- `09_Homebrewery/Book_01/Manuscript/Chapter_00_Explorer_Guild_Primer_Publication_v1.1.md`

## Current PDF Findings

| Page | Finding |
|---|---|
| 1 | Cover renders correctly |
| 2 | Blank reverse page renders correctly |
| 3 | Title page renders correctly |
| 4 | Dedication page renders correctly |
| 5 | Oath page renders correctly |
| 6 | Credits page renders correctly |
| 7 | Contents placeholder renders correctly |
| 8 | Chapter 00 splash page appears to have a missing/broken image |
| 9 | Blank parchment page appears after splash attempt |

## Assembly Fixes Applied

1. Updated Chapter 00 splash image reference from:
   - `Chapter_00_Explorer_Guild_Primer_Splash_Page_v1.0.png`

   to:
   - `Chapter_00_Explorer_Guild_Primer_Splash_Page_v1.1_816x1056.png`

2. Added `.page:has(.chapter00Splash)::after` suppression so page decorations do not display over the splash.

3. Added Chapter 00 body after the splash page.

4. Added sidebar styles:
   - `.guildSidebar`
   - `.contractSidebar`

5. Added structured page breaks between major sections for first render testing.

## Required Render Audit After Paste

After exporting from Homebrewery, check:

- Chapter 00 splash image loads correctly.
- No sidebar overflows.
- No text is clipped at page bottoms.
- Page numbers appear only where desired.
- The contract box in 0.4 fits cleanly.
- Section 0.8 ends cleanly and does not leave an unintended blank page.

## Status

Ready for Homebrewery render test.
