# Hollow Spire Publication Header Framework v1.4

## Locked Rule
Odd / recto publication pages use a right-aligned running header.
Even / verso publication pages use a left-aligned running header.

## Production CSS
Manual `.recto` and `.verso` classes are the source of truth because Homebrewery page wrappers may not always resolve `nth-child` or `nth-of-type` predictably after export.

```css
.hollowRunningHeader.recto { text-align: right !important; }
.hollowRunningHeader.verso { text-align: left !important; }
```

## Chapter 0 Audit Finding
The v1.3 PDF showed the page 9 recto header and page 16 verso header, but pages 10–15 did not reliably display running headers. The v1.4 fix increases z-index, adds `!important`, and assigns explicit recto/verso classes to each running header.
