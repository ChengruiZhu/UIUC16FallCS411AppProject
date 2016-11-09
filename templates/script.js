// Get the Sidenav

function deselect(e) {
  $('.pop').slideFadeToggle(function() {
    e.removeClass('selected');
  });    
}

$(function() {
  $('#contact').on('click', function() {
    if($(this).hasClass('selected')) {
      deselect($(this));               
    } else {
      $(this).addClass('selected');
      $('.pop').slideFadeToggle();
    }
    return false;
  });

  $('.close').on('click', function() {
    deselect($('#contact'));
    return false;
  });
});

$.fn.slideFadeToggle = function(easing, callback) {
  return this.animate({ opacity: 'toggle', height: 'toggle' }, 'fast', easing, callback);
};




//--------------------------------------------------------//






var year={};
function initMap() {
    var myLatLng = {lat: -25.363, lng: 131.044};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Hello World!'
    });

    map.addListener("click", function (event) {
        var latitude = event.latLng.lat();
        var longitude = event.latLng.lng();

        var myLatLng = {lat: latitude, lng: longitude};

        marker.setPosition(myLatLng);
        console.log(latitude + ', ' + longitude);

        // Center of map
        //map.panTo(new google.maps.LatLng(latitude, longitude));

    }); //end addListener
    map.addListener("bounds_changed", function (event) {
        var bounds = map.getBounds();
        var north=bounds.getNorthEast().lat();
        var south=bounds.getSouthWest().lat();
        var west=bounds.getNorthEast().lng();
        var east = bounds.getNorthEast().lng();

    });

}

var main=function() {
    var mySidenav = document.getElementById("mySidenav");

// Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidenav, and add overlay effect
    function w3_open() {
        if (mySidenav.style.display === 'block') {
            mySidenav.style.display = 'none';
            overlayBg.style.display = "none";
        } else {
            mySidenav.style.display = 'block';
            overlayBg.style.display = "block";
        }
    }

// Close the sidenav with the close button
    function w3_close() {
        mySidenav.style.display = "none";
        overlayBg.style.display = "none";
    }



    $('#year').on('click','input', function () {
        var filter = document.getElementById("year");
        console.log(filter);
        for(var i = 0; i < filter.children.length; i++){
            var curr = filter.children[i];
            year[curr.value] = curr.checked?true:false;
        }
        console.log(year);
    });
}
$(document).ready(main);




