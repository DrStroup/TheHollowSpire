# Hollow Spire Header/Footer Rule Update v1.2

STATUS: LOCKED

## Purpose

Corrects the global removal rule for Homebrewery default decorative page ornamentation.

## Rule 1 — Remove Homebrewery Default Decorative Frame Globally

The default Homebrewery page ornamentation must be suppressed on every page.

Required CSS:

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

## Rule 2 — Bottom Art Page Suppression

Bottom-art pages receive an additional page-class marker so they can be targeted explicitly.

Class:
chapter00BottomArtPage

Required behavior:

Header:
YES

Footer:
NO

Page Number:
NO

Explorer Guild Crest:
NO

Homebrewery decorative bottom frame:
NO

## Rule 3 — Running Header Color

All running headers use black text.

Required color:
#000000

## Page 9 Current Implementation

Page 9 is marked as:

chapter00Polish chapter00BottomArtPage

Visible header:
Book I — The Blackwater Warrens

Header color:
#000000

Bottom art:
Chapter_00_Art_01_The_First_Descent_v2

No footer/page number/crest/default Homebrewery ornamentation should appear.
