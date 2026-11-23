// ** grabbing elements from the page **
const navToggle = document.getElementById('navToggle');
const siteNav = document.getElementById('siteNav');

// matches the desktop navigation breakpoint in styles.css
const desktopLayout = window.matchMedia('(min-width: 1160px)');

// ** mobile navigation **
function isNavOpen() {
  return navToggle.getAttribute('aria-expanded') === 'true';
}

function setNavOpen(open) {
  navToggle.setAttribute('aria-expanded', String(open));
  siteNav.classList.toggle('is-open', open);
}

// ** event wiring **
function bindEvents() {
  if (!navToggle || !siteNav) return;

  navToggle.addEventListener('click', () => setNavOpen(!isNavOpen()));

  // Esc closes the menu and returns focus to the toggle button
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && isNavOpen()) {
      setNavOpen(false);
      navToggle.focus();
    }
  });

  // tapping anywhere outside the header closes the menu
  document.addEventListener('click', (event) => {
    if (isNavOpen() && !event.target.closest('.site-header')) {
      setNavOpen(false);
    }
  });

  // reset the menu when the screen widens to the desktop layout
  desktopLayout.addEventListener('change', () => setNavOpen(false));
}

// ** run everything on load **
function initialize() {
  bindEvents();
}

document.addEventListener('DOMContentLoaded', initialize);
