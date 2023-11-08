document.addEventListener("DOMContentLoaded", function() {
  const slides = document.querySelectorAll('.slide');
  let currentSlide = 0;
  let interval;

  function showSlide(index) {
    for (let i = 0; i < slides.length; i++) {
      if (i === index) {
        slides[i].classList.add('active');
      } else {
        slides[i].classList.remove('active');
      }
    }
    currentSlide = index;
  }

  function nextSlide() {
    const nextSlideIndex = (currentSlide + 1) % slides.length;
    showSlide(nextSlideIndex);
  }

  // Adaugă clasa '.active' manual la primul slide.
  slides[0].classList.add('active');

  interval = setInterval(nextSlide, 5000);

  const carouselContainer = document.querySelector('.carousel-container');
  if (carouselContainer) {
    carouselContainer.addEventListener('mouseenter', () => {
      clearInterval(interval);
    });
    carouselContainer.addEventListener('mouseleave', () => {
      interval = setInterval(nextSlide, 5000);
    });
  }
});

document.addEventListener("DOMContentLoaded", function() {
  const images = document.querySelectorAll('.slide img');

  images.forEach((image, index) => {
    image.addEventListener('click', function() {
      if (index === 0) {
        window.location.href = '/plot/';
      } else if (index === 1) {
        window.location.href = '/plot1/';
      }else if (index === 2) {
        window.location.href = '/plot2/';
      }else if (index === 3) {
        window.location.href = '/plot3/';
      }else if (index === 4) {
        window.location.href = '/plot4/';
      }
    });
  });
});



