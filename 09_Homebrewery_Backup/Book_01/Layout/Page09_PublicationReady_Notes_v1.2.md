# Page 09 Publication Ready Notes v1.2

## Issue Corrected

The previous rule used `.page::after { display:none !important; }`, but the rendered PDF still showed Homebrewery's golden bottom filigree on manuscript pages and over the Page 9 bottom artwork.

## Correction

The rule now suppresses both single-colon and double-colon pseudo-elements and removes content, background images, borders, opacity, and shadows.

## Expected Render

- Page 9 should keep the black upper-right running header.
- Page 9 should keep the bottom panorama.
- Page 9 should show no gold Homebrewery filigree over the art.
- Standard manuscript pages should also lose the default gold bottom filigree.
