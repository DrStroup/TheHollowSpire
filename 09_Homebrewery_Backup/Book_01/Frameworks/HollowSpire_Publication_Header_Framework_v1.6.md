# Hollow Spire Publication Header Framework v1.6

## Locked Rule

Running headers alternate by page side:

- Odd / recto pages: right aligned.
- Even / verso pages: left aligned.
- Recto headers use the current chapter title.
- Verso headers use the book / region title.
- Manual `recto` and `verso` classes are the production source of truth.
- Do not rely on `nth-child` or `nth-of-type` in Homebrewery for final production placement.

## CSS

```css
.hollowRunningHeader {
  position: absolute !important;
  top: 18px !important;
  font-size: 10px !important;
  line-height: 1 !important;
  height: 12px !important;
  letter-spacing: .08em !important;
  text-transform: uppercase !important;
  color: #000000 !important;
  -webkit-text-fill-color: #000000 !important;
  font-weight: bold !important;
  z-index: 9999 !important;
  margin: 0 !important;
  padding: 0 !important;
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  pointer-events: none !important;
  white-space: nowrap !important;
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.hollowRunningHeader.recto {
  left: auto !important;
  right: 55px !important;
  width: auto !important;
  text-align: right !important;
}

.hollowRunningHeader.verso {
  left: 55px !important;
  right: auto !important;
  width: auto !important;
  text-align: left !important;
}
```

## Chapter 0 Usage

```html
<div class="hollowRunningHeader recto">Chapter 0 — The Explorer Guild Primer</div>
<div class="hollowRunningHeader verso">Book I — The Blackwater Warrens</div>
```
