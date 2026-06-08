# Chapter 00 Homebrewery Layout Polish Audit v1.0

## Source Reviewed
Current PDF render: `- The Hollow Spire - The Homebrewery(2).pdf`

## Findings
- Chapter 0 renders successfully after the splash.
- Pages 9-16 contain all manuscript sections.
- Layout is readable but many pages are left-heavy.
- Sidebar material renders as plain text rather than styled Guild callouts.

## Polish Actions
- Added Chapter 0-specific CSS.
- Added styled Guild aside boxes.
- Added styled contract box.
- Preserved one page per section.
- Reduced visual left-heaviness by positioning sidebars on the right side of pages.
- Preserved system-neutral publication language.

## Next Step
Paste the replacement block after the Chapter 0 splash, export a fresh PDF, and perform a render audit.
