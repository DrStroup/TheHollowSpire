# Chapter 00 Art 01 — Homebrewery Insert v1.0

## File Added

`09_Homebrewery/Book_01/Art/Chapter_00/Chapter_00_Art_01_The_First_Descent_v1.0.png`

## Raw GitHub URL After Push

`https://raw.githubusercontent.com/DrStroup/TheHollowSpire/main/09_Homebrewery/Book_01/Art/Chapter_00/Chapter_00_Art_01_The_First_Descent_v1.0.png`

## Add this CSS to the Chapter 0 polish style block if not already present

```css
.chapter00MaskedBottomArt {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 44%;
  z-index: 0;
  pointer-events: none;
}

.chapter00Polish {
  position: relative;
  z-index: 1;
}

.chapter00Polish .chapter00MainCol,
.chapter00Polish .guildAside,
.chapter00Polish .contractBox {
  position: relative;
  z-index: 2;
}
```

## Recommended Insert for Page 9 / Section 0.1

Place this inside the first Chapter 0 manuscript page, after the 0.1 text/sidebar block but before the closing `</div>` for the page wrapper.

```markdown
<div class="chapter00MaskedBottomArt">

{{imageMaskEdge4,--offset:10%,--rotation:0
  ![The First Descent](https://raw.githubusercontent.com/DrStroup/TheHollowSpire/main/09_Homebrewery/Book_01/Art/Chapter_00/Chapter_00_Art_01_The_First_Descent_v1.0.png){width:100%,bottom:0%}
}}

</div>
```

## If the image appears too tall

Change:

```markdown
{width:100%,bottom:0%}
```

to:

```markdown
{width:92%,bottom:0%,left:4%}
```

## If the image interferes with text

Lower the art container height:

```css
.chapter00MaskedBottomArt {
  height: 36%;
}
```

## Audit Notes

- Art 01 represents the party overlooking Emberlight from above.
- Emberlight should be interpreted as a small lantern-lit encampment within a vast cavern, not a major city.
- The image has no sky or moon and uses mineral reflections, lanterns, mist, and cavern scale.
- Intended placement: lower portion of Section 0.1 page using Homebrewery watercolor mask.
