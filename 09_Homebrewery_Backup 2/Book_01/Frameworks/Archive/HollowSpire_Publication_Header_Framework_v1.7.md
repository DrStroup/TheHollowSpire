# Hollow Spire Publication Header Framework v1.7

## Locked Running Header Rule

- Odd / recto publication pages use a right-aligned running header.
- Even / verso publication pages use a left-aligned running header.
- Recto header text should identify the current chapter.
- Verso header text should identify the book or region.

## Chapter 0 Header Pair

- Recto / odd pages: `Chapter 0 — The Explorer Guild Primer`
- Verso / even pages: `Book I — The Blackwater Warrens`

## Homebrewery Implementation Rule

Do not rely on `nth-child`, `nth-of-type`, or compound classes such as `.hollowRunningHeader.recto` for production headers. Homebrewery page wrappers can behave unpredictably after masked images, absolute elements, and page breaks.

Use one-purpose header classes:

```css
.hollowHeaderRight {
  position: absolute !important;
  top: 18px !important;
  right: 55px !important;
  text-align: right !important;
}

.hollowHeaderLeft {
  position: absolute !important;
  top: 18px !important;
  left: 55px !important;
  text-align: left !important;
}
```

## Page Placement Pattern

```html
\page
<div class="hollowHeaderRight">Chapter 0 — The Explorer Guild Primer</div>
```

```html
\page
<div class="hollowHeaderLeft">Book I — The Blackwater Warrens</div>
```

## Audit Note

If a rendered PDF shows repeated or incorrect header text after the source has been updated, clear the Homebrewery render/cache and re-export. The v1.7 framework removes the previous compound-class ambiguity.
