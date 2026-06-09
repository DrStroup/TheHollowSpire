<style>
.creditsPageAsset {
  position: absolute;
  inset: 0;
  background: white;
  z-index: 100;
}

.creditsPageAsset img {
  position: absolute;
  top: 0;
  left: 50%;
  width: auto;
  height: 100%;
  transform: translateX(-50%);
}

.page:has(.creditsPageAsset)::after,
.page:has(.creditsPageAsset) .pageNumber,
.page:has(.creditsPageAsset) .footnote {
  display: none !important;
}
</style>

<div class="creditsPageAsset">
  <img src="https://raw.githubusercontent.com/DrStroup/TheHollowSpire/main/09_Homebrewery/Book_01/Art/Credits/Credits_Page_v1.0.png">
</div>

\page
