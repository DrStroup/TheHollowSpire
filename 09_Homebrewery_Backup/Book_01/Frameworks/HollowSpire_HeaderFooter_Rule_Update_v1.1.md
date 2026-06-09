# Hollow Spire Header/Footer Rule Update v1.1

STATUS: LOCKED

## Purpose

This update refines the Hollow Spire publication header/footer rules based on the Page 9 publication pass.

## Rule 1 — Running Header Color

All running headers use black text.

Required color:

#000000

Reason:
Running headers are navigational elements, not chapter accent elements. Chapter titles may retain the Hollow Spire red/brown accent, but running headers should remain clean, readable, and publication-neutral.

## Rule 2 — Remove Homebrewery Default Decorative Frame

The default Homebrewery decorative page ornamentation is removed globally.

Required CSS:

.page::after {
  display:none !important;
}

Reason:
The Hollow Spire uses its own visual language, artwork, page furniture, and layout system. Homebrewery's default bottom ornamentation should not appear on any page unless intentionally reintroduced as a custom Hollow Spire asset.

## Rule 3 — Bottom Art Pages

Bottom art pages retain the running header but do not show footer furniture.

Header:
YES

Footer:
NO

Page Number:
NO

Explorer Guild Crest:
NO

Reason:
Bottom artwork functions as the visual footer.

## Rule 4 — Page 9 Implementation

Page 9 is a right-hand bottom-art page.

Visible header:
Book I — The Blackwater Warrens

Header color:
#000000

Footer/page number/crest:
None

Bottom artwork:
Chapter_00_Art_01_The_First_Descent_v2

## Implementation Notes

For current Homebrewery workflow, full-book replacement text files are preferred over partial snippets.

The corresponding full replacement Homebrewery source is:

Homebrewery_Code_The_Hollow_Spire_Page09_PublicationReady_v1.1_FULL_REPLACE.txt
