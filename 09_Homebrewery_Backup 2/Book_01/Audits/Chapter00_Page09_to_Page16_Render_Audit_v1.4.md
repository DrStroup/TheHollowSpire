# Chapter 00 Page 9–16 Render Audit v1.4

## Findings
- Page 9: running header appears correctly on the right.
- Page 16: running header appears correctly on the left.
- Pages 10–15: running headers were not reliably visible in the supplied render.
- Chapter 0 body headings still rendered red in the supplied PDF despite the v1.3 source setting headings to black.

## Fixes Applied
- Strengthened Chapter 0 heading color rules with `!important`.
- Added explicit `.recto` and `.verso` running header classes.
- Raised running header z-index to 999.
- Preserved global Homebrewery decorative filigree suppression.

## Required Verification
Export a fresh PDF from Homebrewery using v1.4 source and verify:
- Page 9 header: right aligned.
- Page 10 header: left aligned.
- Page 11 header: right aligned.
- Page 12 header: left aligned.
- Page 13 header: right aligned.
- Page 14 header: left aligned.
- Page 15 header: right aligned.
- Page 16 header: left aligned.
- Chapter 0 section headings render black unless intentionally changed back to red.
