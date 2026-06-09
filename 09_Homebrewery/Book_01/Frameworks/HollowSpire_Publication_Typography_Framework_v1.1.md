# Hollow Spire Publication Typography Framework v1.1

## Locked Running Header Rule

Even-numbered pages use left-aligned running headers. Odd-numbered pages use right-aligned running headers.

Running headers must be black, uppercase, small-sized, and positioned consistently across publication pages.

```css
.hollowRunningHeader {
  position: absolute;
  top: 30px;
  left: 55px;
  right: 55px;
  font-size: 10px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #000000;
  font-weight: bold;
  z-index: 20;
}

.page:nth-of-type(odd) .hollowRunningHeader,
.page:nth-child(odd) .hollowRunningHeader {
  text-align: right;
}

.page:nth-of-type(even) .hollowRunningHeader,
.page:nth-child(even) .hollowRunningHeader {
  text-align: left;
}
```

## Locked Decorative Suppression Rule

All Homebrewery default footer filigree and pseudo-element decoration must be suppressed globally.

```css
.page::after,
.page:after,
.page::before,
.page:before {
  content: none !important;
  display: none !important;
  background: none !important;
  background-image: none !important;
  border: none !important;
  box-shadow: none !important;
  opacity: 0 !important;
}
```

## Chapter 0 Page 9 Audit Notes

- Running header converted from one-off inline styling to global framework class.
- Odd page alignment is right-aligned by CSS.
- Even page alignment is left-aligned by CSS.
- Chapter 0 body headings changed from red to black for the current production direction.
- Default Homebrewery filigree remains globally suppressed.
