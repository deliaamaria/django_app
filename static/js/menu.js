document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    let menuVisible = false;

    window.addEventListener('scroll', function() {
      if (window.scrollY > 10) {
        // Dacă s-a derulat în jos, afișează iconița meniului
        menuToggle.style.display = 'block';
      } else {
        // Dacă a revenit în partea de sus, ascunde iconița meniului și meniul mobil
        menuToggle.style.display = 'none';
        mobileMenu.style.display = 'none';
        menuVisible = false;
      }
    });

    menuToggle.addEventListener('click', function() {
      // Comută între meniul normal și meniul mobil când butonul hamburger este apăsat
      if (menuVisible) {
        mobileMenu.style.display = 'none';
        menuVisible = false;
      } else {
        mobileMenu.style.display = 'block';
        menuVisible = true;
      }
    });

     document.addEventListener('click', function(event) {
    if (event.target !== menuToggle && event.target !== mobileMenu) {
      // Dacă s-a făcut clic în afara butonului de meniu sau a meniului mobil, ascunde meniul
      mobileMenu.style.display = 'none';
      menuVisible = false;
    }
  });
  });