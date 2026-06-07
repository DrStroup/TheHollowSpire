<style>
.oathPageAsset {
  position: absolute;
  inset: 0;
  background: white;
  z-index: 100;
}

.oathPageAsset img {
  position: absolute;
  top: 0;
  left: 50%;
  width: auto;
  height: 100%;
  transform: translateX(-50%);
}

.page:has(.oathPageAsset)::after,
.page:has(.oathPageAsset) .pageNumber,
.page:has(.oathPageAsset) .footnote {
  display: none !important;
}
</style>

<div class="oathPageAsset">
  <img src="https://raw.githubusercontent.com/DrStroup/TheHollowSpire/main/09_Homebrewery/Book_01/Art/Explorer_Guild_Oath/Oath_of_the_Explorers_Guild_Page_v1.0.png">
</div>

\page
