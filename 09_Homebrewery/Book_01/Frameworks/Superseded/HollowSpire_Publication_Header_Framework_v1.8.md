# Hollow Spire Publication Header Framework v1.8

## Locked Running Header Rule

Chapter publication pages use alternating running headers:

- Odd / recto pages: right aligned, current chapter title.
- Even / verso pages: left aligned, book/region title.

For Chapter 0:

- Right header text: `Chapter 0 — The Explorer Guild Primer`
- Left header text: `Book I — The Blackwater Warrens`

## Production Implementation Rule

Homebrewery can behave unpredictably with page wrapper selectors, compound classes, and global CSS inheritance across later pages. Beginning with v1.8, the production-safe source of truth is an inline-positioned header block on each page.

Use:

```html
<div class="hollowHeaderRight" style="position:absolute !important; top:18px !important; right:55px !important; left:auto !important; width:auto !important; font-size:10px !important; line-height:1 !important; height:12px !important; letter-spacing:.08em !important; text-transform:uppercase !important; color:#000000 !important; -webkit-text-fill-color:#000000 !important; font-weight:bold !important; z-index:99999 !important; margin:0 !important; padding:0 !important; display:block !important; visibility:visible !important; opacity:1 !important; pointer-events:none !important; white-space:nowrap !important; background:transparent !important; border:0 !important; box-shadow:none !important; text-align:right !important;">Chapter 0 — The Explorer Guild Primer</div>
```

for odd / recto pages, and:

```html
<div class="hollowHeaderLeft" style="position:absolute !important; top:18px !important; left:55px !important; right:auto !important; width:auto !important; font-size:10px !important; line-height:1 !important; height:12px !important; letter-spacing:.08em !important; text-transform:uppercase !important; color:#000000 !important; -webkit-text-fill-color:#000000 !important; font-weight:bold !important; z-index:99999 !important; margin:0 !important; padding:0 !important; display:block !important; visibility:visible !important; opacity:1 !important; pointer-events:none !important; white-space:nowrap !important; background:transparent !important; border:0 !important; box-shadow:none !important; text-align:left !important;">Book I — The Blackwater Warrens</div>
```

for even / verso pages.

## Do Not Use

Do not rely on `nth-child`, `nth-of-type`, or compound `.recto` / `.verso` selectors as the production source of truth in Homebrewery.
