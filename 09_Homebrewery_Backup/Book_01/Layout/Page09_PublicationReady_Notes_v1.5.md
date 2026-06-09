# Page 9 Publication Notes v1.5

## Current Audit Result

The v1.4 PDF showed:
- Page 9 running header visible and correctly right aligned.
- Page 15 running header visible and correctly right aligned.
- Page 16 running header visible and correctly left aligned.
- Pages 10–14 did not visibly render running headers despite source elements being present.
- Chapter 0 headings continued to render red despite the v1.4 black CSS override.

## v1.5 Fix

- Removed dependency on Homebrewery page parity selectors for production behavior.
- Kept only manual `.recto` and `.verso` positioning as the source of truth.
- Moved running headers to `top: 18px` to avoid collisions with page heading layout.
- Added explicit `display`, `visibility`, `opacity`, `white-space`, `line-height`, and `-webkit-text-fill-color` declarations.
- Strengthened Chapter 0 heading override to include nested spans, text fill, text shadow, and border color.
