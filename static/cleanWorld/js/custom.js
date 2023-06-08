$(function() {
    "use strict";

    $(".preloader").fadeOut();
    $(".nav-toggler").on('click', function() {
        $("#main-wrapper").toggleClass("show-sidebar");
        $(".nav-toggler i").toggleClass("ti-menu");
    });
    $(".search-box a, .search-box .app-search .srh-btn").on('click', function() {
        $(".app-search").toggle(200);
        $(".app-search input").focus();
    });

    $("body, .page-wrapper").trigger("resize");
    $(".page-wrapper").delay(20).show();
    
    var setsidebartype = function() {
        var width = (window.innerWidth > 0) ? window.innerWidth : this.screen.width;
        if (width < 1170) {
            $("#main-wrapper").attr("data-sidebartype", "mini-sidebar");
        } else {
            $("#main-wrapper").attr("data-sidebartype", "full");
        }
    };
    $(window).ready(setsidebartype);
    $(window).on("resize", setsidebartype);

});

    var addressObj = document.getElementById('address');

    var lp = new locationPicker('map', {
        setCurrentPosition: true,
    }, {
    zoom: 15,
    center: new google.maps.LatLng(35.6892, 51.3890),
    zoomControl: true,
    zoomControlOptions: {
      style: google.maps.ZoomControlStyle.DEFAULT,
    },
    disableDoubleClickZoom: true,
    mapTypeControl: true,
    scaleControl: true,
    scrollwheel: true,
    panControl: true,
    streetViewControl: false,
    draggable: true,
    overviewMapControl: true,
    overviewMapControlOptions: {
      opened: true,
    },
    mapTypeId: google.maps.MapTypeId.HYBRID,
    });

    google.maps.event.addListener(lp.map, 'idle', function (event) {
    var location = lp.getMarkerPosition();
        connect(location.lat, location.lng);
    });


function connect(lat, long) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `https://api.neshan.org/v2/reverse?lat=${lat}&lng=${long}`);
    xhr.setRequestHeader('Api-Key', 'service.oYtbKgkeoCjaMADbPljOuKqLbxDU7sHAP6GDdquq')
    xhr.timeout = 10000;
    xhr.ontimeout = function () { console.log('time out'); }
    xhr.responseType = 'json';

    xhr.onreadystatechange = function(e) {
        if (this.status === 200 && xhr.readyState == 4) {
            res = this.response;
            var addressObj = document.getElementById('address');
            var coordinatesObj = document.getElementById('coordinates');
            addressObj.value = res['formatted_address']
            coordinatesObj.value = `${lat},${long}`

        }
        else {
            console.log(this.status)
        }
    };
    try {
        xhr.send();
    } catch(err) {
        console.log('error')
    }
}