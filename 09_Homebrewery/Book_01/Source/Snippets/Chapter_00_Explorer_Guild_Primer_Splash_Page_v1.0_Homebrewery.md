<style>
.chapter00SplashPage {
  position: absolute;
  inset: 0;
  background: black;
  z-index: 100;
}

.chapter00SplashPage img {
  position: absolute;
  top: 0;
  left: 50%;
  width: auto;
  height: 100%;
  transform: translateX(-50%);
}

.page:has(.chapter00SplashPage)::after,
.page:has(.chapter00SplashPage) .pageNumber,
.page:has(.chapter00SplashPage) .footnote {
  display: none !important;
}
</style>

<div class="chapter00SplashPage">
  <img src="https://raw.githubusercontent.com/DrStroup/TheHollowSpire/main/09_Homebrewery/Book_01/Art/Chapter_00/Chapter_00_Explorer_Guild_Primer_Splash_Page_v1.0.png">
</div>

\page
