// HEADER ANIMATION
window.onscroll = function() {scrollFunction()};
var element = document.getElementById("body");
function scrollFunction() {
  if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
	  $(".navbar").addClass("fixed-top");
	  element.classList.add("header-small");
	  $("body").addClass("body-top-padding");

  } else {
	  $(".navbar").removeClass("fixed-top");
	  element.classList.remove("header-small");
	  $("body").removeClass("body-top-padding");
  }
}

// OWL-CAROUSAL
$('.owl-carousel').owlCarousel({
	items: 3,
	loop:true,
	nav:false,
	dot:true,
	autoplay: true,
	slideTransition: 'linear',
	autoplayHoverPause: true,
	responsive:{
	  0:{
		  items:1
	  },
	  600:{
		  items:2
	  },
	  1000:{
		  items:3
	  }
  }
})

// SCROLLSPY
$(document).ready(function() {
  $(".nav-link").click(function() {
	  var t = $(this).attr("href");
	  $("html, body").animate({
		  scrollTop: $(t).offset().top - 75
	  }, {
		  duration: 1000,
	  });
	  $('body').scrollspy({ target: '.navbar',offset: $(t).offset().top });
	  return false;
  });

});

// AOS
AOS.init({
	offset: 120, 
	delay: 0,
	duration: 1200, 
	easing: 'ease', 
	once: true, 
	mirror: false, 
	anchorPlacement: 'top-bottom', 
	disable: "mobile"
  });

//SIDEBAR-OPEN
  $('#navbarSupportedContent').on('hidden.bs.collapse', function () {
	$("body").removeClass("sidebar-open");
  })

  $('#navbarSupportedContent').on('shown.bs.collapse', function () {
	$("body").addClass("sidebar-open");
  })


  window.onresize = function() {
	var w = window.innerWidth;
	if(w>=992) {
	  $('body').removeClass('sidebar-open');
	  $('#navbarSupportedContent').removeClass('show');
	}
  }

var TxtType = function(el, toRotate, period) {
	  this.toRotate = toRotate;
	  this.el = el;
	  this.loopNum = 0;
	  this.period = parseInt(period, 10) || 20000;
	  this.txt = '';
	  this.tick();
	  this.isDeleting = false;
  };

  TxtType.prototype.tick = function() {
	  var i = this.loopNum % this.toRotate.length;
	  var fullTxt = this.toRotate[i];

	  if (this.isDeleting) {
	  this.txt = fullTxt.substring(0, this.txt.length - 1);
	  } else {
	  this.txt = fullTxt.substring(0, this.txt.length + 1);
	  }

	  this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

	  var that = this;
	  var delta = 200 - Math.random() * 100;

	  if (this.isDeleting) { delta /= 2; }

	  if (!this.isDeleting && this.txt === fullTxt) {
	  delta = this.period;
	  this.isDeleting = true;
	  } else if (this.isDeleting && this.txt === '') {
	  this.isDeleting = false;
	  this.loopNum++;
	  delta = 500;
	  }

	  setTimeout(function() {
	  that.tick();
	  }, delta);
  };

  window.onload = function() {
	  var elements = document.getElementsByClassName('typewrite');
	  for (var i=0; i<elements.length; i++) {
		  var toRotate = elements[i].getAttribute('data-type');
		  var period = elements[i].getAttribute('data-period');
		  if (toRotate) {
			new TxtType(elements[i], JSON.parse(toRotate), period);
		  }
	  }
	  // INJECT CSS
	  var css = document.createElement("style");
	  css.type = "text/css";
	  css.innerHTML = ".typewrite > .wrap { border-left: 0.08em solid white}";
	  document.body.appendChild(css);
  };