(function($) {
  
  "use strict";  

  $(window).on('load', function() {

  /*Page Loader active
    ========================================================*/
    $('#preloader').delay("fast").fadeOut();
  
  // Sticky Nav
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 200) {
            $('.scrolling-navbar').addClass('top-nav-collapse');
        } else {
            $('.scrolling-navbar').removeClass('top-nav-collapse');
        }
    });

    /* ==========================================================================
       countdown timer
       ========================================================================== */
     jQuery('#clock').countdown('2019/11/24 08:30:00',function(event){
      var $this=jQuery(this).html(event.strftime(''
      +'<div class="time-entry days"><span>%-D</span> <b>:</b> Days</div> '
      +'<div class="time-entry hours"><span>%H</span> <b>:</b> Hours</div> '
      +'<div class="time-entry minutes"><span>%M</span> <b>:</b> Minutes</div> '
      +'<div class="time-entry seconds"><span>%S</span> Seconds</div> '));
    });

    /* Auto Close Responsive Navbar on Click
    ========================================================*/
    function close_toggle() {
              $('.navbar .navbar-inverse a').off('click');
    }
    close_toggle();
    $(window).resize(close_toggle);




      /* WOW Scroll Spy
    ========================================================*/
     var wow = new WOW({
      //disabled for mobile
        mobile: false
    });
    wow.init();

    /* Nivo Lightbox 
    ========================================================*/
    $('.lightbox').nivoLightbox({
        effect: 'fadeScale',
        keyboardNav: true,
      });

    // one page navigation 
    $('.navbar-nav').onePageNav({
            currentClass: 'active'
    }); 

    /* Counter
    ========================================================*/
    $('.counterUp').counterUp({
     delay: 10,
     time: 1500
    });

    /* Back Top Link active
    ========================================================*/
      var offset = 200;
      var duration = 500;
      $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
          $('.back-to-top').fadeIn(400);
        } else {
          $('.back-to-top').fadeOut(400);
        }
      });

      $('.back-to-top').on('click',function(event) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: 0
        }, 600);
        return false;
      });

  });      

}(jQuery));


$("#js-rotating").Morphext({
  // The [in] animation type. Refer to Animate.css for a list of available animations.
  animation: "bounceIn",
  // An array of phrases to rotate are created based on this separator. Change it if you wish to separate the phrases differently (e.g. So Simple | Very Doge | Much Wow | Such Cool).
  separator: ",",
  // The delay between the changing of each phrase in milliseconds.
  speed: 3000,
  complete: function () {
      // Called after the entrance animation is executed.
  }
});

 /* Button Tooltip
    ========================================================*/

    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })

/* Jquery Add active class to main menu
    ========================================================*/


    $('.carousel').carousel()

    $('#myTab a').on('click', function (e) {
      e.preventDefault()
      $(this).tab('show')
    })

/*   Custom Notification
    ========================================================*/
    setInterval(function(){ $(".custom-social-proof").stop().slideToggle('slow'); }, 2000);
    clearInterval(".custom-social-proof");
    $(".custom-close").click(function() {
      $(".custom-social-proof").stop().slideToggle('slow');
    });

    setInterval(function(){ $(".custom-social-proof2").stop().slideToggle('slow'); }, 3000);
    clearInterval(".custom-social-proof2");
    $(".custom-close").click(function() {
      $(".custom-social-proof2").stop().slideToggle('slow');
    });

    setInterval(function(){ $(".custom-social-proof3").stop().slideToggle('slow'); }, 4000);
    clearInterval(".custom-social-proof3");
    $(".custom-close").click(function() {
      $(".custom-social-proof3").stop().slideToggle('slow');
    });

    setInterval(function(){ $(".custom-social-proof4").stop().slideToggle('slow'); }, 8000);
    clearInterval(".custom-social-proof4");
    $(".custom-close").click(function() {
      $(".custom-social-proof4").stop().slideToggle('slow');
    });

    setInterval(function(){ $(".custom-social-proof5").stop().slideToggle('slow'); }, 12000);
    clearInterval(".custom-social-proof5");
    $(".custom-close").click(function() {
      $(".custom-social-proof5").stop().slideToggle('slow');
    });


