const menuHamburguer = document.querySelector('.menu-hamburguer');
const menuMobile = document.querySelector('.menu-mobile-content');

menuHamburguer.addEventListener('mouseenter', () => {
  menuMobile.classList.add('show');
});

menuHamburguer.addEventListener('mouseleave', () => {
  setTimeout(() => {
    if (!menuMobile.matches(':hover')) {
      menuMobile.classList.remove('show');
    }
  }, 300); 
});

menuMobile.addEventListener('mouseleave', () => {
  menuMobile.classList.remove('show');
});