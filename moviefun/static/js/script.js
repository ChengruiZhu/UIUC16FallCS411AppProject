// Get the Sidenav
var list;
var year={'1980': true,'1990': true,'2000':true};
var genre={'Action': true,'Drama': true,'Romance':true};
var ratings={'6.0': true,'7.0': true,'8.0':true};
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


var map;
var markers = [];



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

    }); //end addListener
    map.addListener("bounds_changed", function (event) {
        var bounds = map.getBounds();
        var north=bounds.getNorthEast().lat();
        var south=bounds.getSouthWest().lat();
        var west=bounds.getNorthEast().lng();
        var east = bounds.getNorthEast().lng();

    });
    function addMarker(location) {
        var marker = new google.maps.Marker({
            position: location,
            map: map
        });
        markers.push(marker);
    }

    // Sets the map on all markers in the array.
    function setMapOnAll(map) {
        for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(map);
        }
    }

    // Removes the markers from the map, but keeps them in the array.
    function clearMarkers() {
        setMapOnAll(null);
    }

    // Shows any markers currently in the array.
    function showMarkers() {
        setMapOnAll(map);
    }

    // Deletes all markers in the array by removing references to them.
    function deleteMarkers() {
        clearMarkers();
        markers = [];
    }

}

var main=function() {
    getData();
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
        var ct=0
        for(var i = 0; i < filter.children.length; i++){
            var curr = filter.children[i].children[0];
            if(!curr.checked) ct++;
            year[curr.value] = curr.checked?true:false;
        }
        if(ct==3){
            year={'1980': true,'1990': true,'2000':true};
        }
        var param = {'year':year, 'genre': genre,'rating': ratings};
        console.log(param);
    });
    $('#genre').on('click','input', function () {
        var filter = document.getElementById("genre");
        //count if all false
        var ct=0;
        for(var i = 0; i < filter.children.length; i++){
            var curr = filter.children[i].children[0];
            if(!curr.checked) ct++;
            genre[curr.value] = curr.checked?true:false;
        }
        if(ct==3){
            genre={'Action': true,'Drama': true,'Romance':true};
        }
        var param = {'year':year, 'genre': genre,'rating': ratings};
        console.log(param);
    });
    $('#ratings').on('click','input', function () {
        var filter = document.getElementById("ratings");
        var ct=0;
        for(var i = 0; i < filter.children.length; i++){
            var curr = filter.children[i].children[0];
            if(!curr.checked) ct++;
            ratings[curr.value] = curr.checked?true:false;
        }
        if(ct==3){
            ratings={'6.0': true,'7.0': true,'8.0':true};
        }
        var param = {'year':year, 'genre': genre,'rating': ratings};
        console.log(param);
    });
}
function query() {
    $({
        method: "GET",
        url: "/imdb250.json"
    }).then(function mySucces(response) {
        list = response.data;
    }, function myError(response) {
        list = response.statusCode;
    });

}
function getData(){
    /*$.get("./imdb250.json", { name: "John", time: "2pm" } )
        .done(function(data, status){
        list=data[0];
    });*/
    $.get("./imdb250.json", function(data, status){
        list=data[0];
    });
}

$(document).ready(main);



