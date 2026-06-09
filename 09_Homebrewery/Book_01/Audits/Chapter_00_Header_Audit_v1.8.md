# Chapter 0 Header Audit v1.8

## Root Cause

The v1.7 PDF confirmed that the intended left/right header text was correct in source, but later rendered pages did not consistently honor the shared header class styling. The most visible symptom was that pages 14-16 showed headers dropping into normal page flow rather than remaining locked to the absolute running-header position.

## Fix

v1.8 converts every Chapter 0 text-page header into a fully inline-positioned production header. The class names remain for readability, but the inline style is now the production source of truth.

## Expected Render

- Page 9: right header, `Chapter 0 — The Explorer Guild Primer`
- Page 10: left header, `Book I — The Blackwater Warrens`
- Page 11: right header, `Chapter 0 — The Explorer Guild Primer`
- Page 12: left header, `Book I — The Blackwater Warrens`
- Page 13: right header, `Chapter 0 — The Explorer Guild Primer`
- Page 14: left header, `Book I — The Blackwater Warrens`
- Page 15: right header, `Chapter 0 — The Explorer Guild Primer`
- Page 16: left header, `Book I — The Blackwater Warrens`

## Status

Ready for Homebrewery paste-and-render verification.
