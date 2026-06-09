# Hollow Spire Publication Typography Framework v1.5

## Running Headers

Locked rule:
- Odd / recto publication pages use right-aligned running headers.
- Even / verso publication pages use left-aligned running headers.
- Manual `.recto` and `.verso` classes are the production source of truth.
- Do not rely on `nth-child` or `nth-of-type` for Homebrewery production exports because generated page wrappers can behave unpredictably.

CSS source of truth is embedded in `Book_01_Homebrewery_Source_v1.5.md`.

## Chapter Heading Color

Chapter body headings must render black in production PDF exports unless a chapter-specific art page intentionally uses another treatment.

The v1.5 rule targets:
- `color`
- `-webkit-text-fill-color`
- `text-shadow`
- `border-color`

This is required because Homebrewery can apply red heading styling through nested spans or browser text-fill behavior.

## Decorative Footer Suppression

Homebrewery default gold filigree is globally suppressed through both `::before` and `::after` pseudo-element rules.
