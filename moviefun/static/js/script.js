// Get the Sidenav
var list;
var year={'1980': true,'1990': true,'2000':true};
var genre={'Action': true,'Drama': true,'Romance':true};
var ratings={'6.0': true,'7.0': true,'8.0':true};
//for click blank space, popup disappears
// function deselect(e) {
//   $('.pop').slideFadeToggle(function() {
//     e.removeClass('selected');
//   });    
// }

// $(function() {
//   $('#contact').on('click', function() {
//     if($(this).hasClass('selected')) {
//       deselect($(this));               
//     } else {
//       $(this).addClass('selected');
//       $('.pop').slideFadeToggle();
//     }
//     return false;
//   });

//   $('.close').on('click', function() {
//     deselect($('#contact'));
//     return false;
//   });
// });

// $.fn.slideFadeToggle = function(easing, callback) {
//   return this.animate({ opacity: 'toggle', height: 'toggle' }, 'fast', easing, callback);
// };

var map;
var markers = [];

var north;
var south;
var west;
var east;

var year={};
function initMap() {
    myLatLng = {lat: -25.363, lng: 131.044};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: myLatLng
    });

    var infowindow = new google.maps.InfoWindow({
        content: null
    });
    
    function addMarker(movie) {
        var marker = new google.maps.Marker({
            position: {lat: Number(movie["latitude"]),
                        lng: Number(movie["longitude"])},
            map: map
        });

        marker.addListener('click', function() {
            var str="<p>"+movie['title']+"</p><button id='likes' value ="+movie['imdbid']+" >me</button>"
            
            var btn = document.getElementById('likes');

            

            infowindow.setContent(str);
            infowindow.open(map, marker);

            $('#likes').on('click', function(){
                console.log(2);
                var btn = document.getElementById('likes');
                console.log(btn.value);
                like(btn.value);

            });
        });
        markers.push(marker);
    }
  
    function boundChange(){
        getData(function() {
            for (var i = 0; i < list.length; i++) {
                addMarker(list[i]);
            }
        });     
    }

    map.addListener("bounds_changed", function (event) {
        var bounds = map.getBounds();
        north=bounds.getNorthEast().lat();
        south=bounds.getSouthWest().lat();
        west=bounds.getNorthEast().lng();
        east = bounds.getSouthWest().lng();
        boundChange();
        setMapOnAll(map);
        showMarkers();

    });
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
    var mySidenav = document.getElementById("mySidenav");

// Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");
    /*$('#likes').on('click', function(){
        btn = getElementById('likes');
        console.log(2);
        console.log(btn.value);
        like(btn.value);
    });*/


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
        var ct=0;
        for(var i = 0; i < filter.children.length; i++){
            var curr = filter.children[i].children[0];
            if(!curr.checked) ct++;
            year[curr.value] = curr.checked?true:false;
        }
        if(ct==3){
            year={'1980': true,'1990': true,'2000':true};
        }
        var param = {'year':year, 'genre': genre,'rating': ratings};
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
function getData(callback){

    /*$.get("http://fa16-cs411-04.cs.illinois.edu:8000/moviefun/get/200.0/240.0/50.0/70.0/", function(data, status){
        list = data;
        // console.log(data);
    });*/
    $.get("http://fa16-cs411-04.cs.illinois.edu:8000/moviefun/get/"+
           (north+180.0).toString()+"/"+(south+180.0).toString()+"/"+
           (west+180.0).toString()+"/"+(east+180.0).toString()+"/", function(data, status){
        list = data;
        // console.log(data);
    });

    callback();    
}
function like(movieID){
    $.get("http://fa16-cs411-04.cs.illinois.edu:8000/moviefun/like/"+movieID, function(){
    });
}

$(document).ready(main);
