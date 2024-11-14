(function ($) {
  "use strict";

  // Search Popup functionality
  var searchPopup = function () {
    // Toggle search popup visibility
    $("#header-nav").on(
      "click",
      ".search-button, .btn-close-search",
      function (e) {
        $(".search-popup").toggleClass("is-visible");
      }
    );

    // Open search popup with focus on search input
    $(".search-popup-trigger").on("click", function (e) {
      e.preventDefault();
      $(".search-popup").addClass("is-visible");
      setTimeout(function () {
        $(".search-popup").find("#search-popup").focus();
      }, 350);
    });

    // Close search popup when clicking outside or pressing 'Esc'
    $(".search-popup").on("click", function (e) {
      if (
        $(e.target).is(".search-popup-close") ||
        $(e.target).is(".search-popup") ||
        e.key === "Escape"
      ) {
        $(".search-popup").removeClass("is-visible");
      }
    });
  };

  // Initialize Product Quantity functionality
  var initProductQty = function () {
    $(".product-qty").each(function () {
      var $el_product = $(this);

      $el_product.find(".quantity-right-plus").click(function (e) {
        e.preventDefault();
        var quantity = parseInt($el_product.find("#quantity").val());
        $el_product.find("#quantity").val(quantity + 1);
      });

      $el_product.find(".quantity-left-minus").click(function (e) {
        e.preventDefault();
        var quantity = parseInt($el_product.find("#quantity").val());
        if (quantity > 0) {
          $el_product.find("#quantity").val(quantity - 1);
        }
      });
    });
  };

  // Document Ready Function
  $(document).ready(function () {
    searchPopup();
    initProductQty();

    // Initialize main Swiper for featured products
    new Swiper(".main-swiper", {
      loop: true,
      autoplay: {
        delay: 3000,
        disableOnInteraction: false,
      },
      pagination: { el: ".swiper-pagination", clickable: true },
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        768: { slidesPerView: 2 }, // Show two items on tablets and up
        992: { slidesPerView: 3 }, // Show three items on larger screens
      },
    });

    // Initialize product Swiper for general products
    new Swiper(".product-swiper", {
      slidesPerView: 1, // Show one product at a time on mobile
      spaceBetween: 10,
      pagination: { el: ".swiper-pagination", clickable: true },
      breakpoints: {
        768: { slidesPerView: 2 }, // Show two items on tablets
        992: { slidesPerView: 4 }, // Show four items on desktops
      },
    });

    // Initialize specific product watch Swiper
    new Swiper(".product-watch-swiper", {
      slidesPerView: 1,
      spaceBetween: 10,
      pagination: {
        el: "#smart-watches .swiper-pagination",
        clickable: true,
      },
      breakpoints: {
        768: { slidesPerView: 2 },
        980: { slidesPerView: 4 },
      },
    });

    // Initialize testimonial Swiper with loop and navigation
  });

  document.addEventListener("DOMContentLoaded", function () {
    const swiper = new Swiper(".main-swiper", {
      // Swiper options
      loop: true,
      autoplay: {
        delay: 5000, // 5 seconds
        disableOnInteraction: false,
      },
      slidesPerView: 1,
      spaceBetween: 10,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
  });
  var swiper = new Swiper(".swiper-container", {
    slidesPerView: 1,
    spaceBetween: 10,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
})(jQuery);
