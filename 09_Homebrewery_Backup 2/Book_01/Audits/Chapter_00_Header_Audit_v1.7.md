# Chapter 0 Header Audit v1.7

## Render Issue Observed

The v1.6 source contains alternating recto/verso header text, but the attached PDF still shows repeated `Book I — The Blackwater Warrens` on later pages where `Chapter 0 — The Explorer Guild Primer` should appear.

## Root Cause Assessment

The source itself is structurally close, but the compound class approach:

```html
<div class="hollowRunningHeader recto">...</div>
<div class="hollowRunningHeader verso">...</div>
```

is less reliable in Homebrewery than separate one-purpose classes, especially across page breaks following absolute-positioned content and masked images.

## v1.7 Fix

Replaced compound classes with:

```html
<div class="hollowHeaderRight">Chapter 0 — The Explorer Guild Primer</div>
<div class="hollowHeaderLeft">Book I — The Blackwater Warrens</div>
```

## Expected Render

- Page 9: Chapter 0 — The Explorer Guild Primer, right aligned.
- Page 10: Book I — The Blackwater Warrens, left aligned.
- Page 11: Chapter 0 — The Explorer Guild Primer, right aligned.
- Page 12: Book I — The Blackwater Warrens, left aligned.
- Page 13: Chapter 0 — The Explorer Guild Primer, right aligned.
- Page 14: Book I — The Blackwater Warrens, left aligned.
- Page 15: Chapter 0 — The Explorer Guild Primer, right aligned.
- Page 16: Book I — The Blackwater Warrens, left aligned.
