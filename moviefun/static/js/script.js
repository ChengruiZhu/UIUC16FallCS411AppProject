// Get the Sidenav
var list;
var year=[1900,2016];
var genre={'Action': true,'Adventure': true,'Crime': true,'Drama': true,'Musical': true,'Romance': true,'Western':true};
var ratings=[0.0,10.0];

var markers = [];

var north;
var south;
var west;
var east;
var id;
var gmovie;

var year={};
function initMap() {
    myLatLng = {lat: -25.363, lng: 131.044};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: myLatLng
    });

    var infowindow = new google.maps.InfoWindow({
        content: null,
        disableAutoPan: true
    });

    /*$('#Like').on('click', function(){
        like(id);
    });*/

    function addMarker(movie) {
        var marker = new google.maps.Marker({
            position: {lat: Number(movie["latitude"]),
                        lng: Number(movie["longitude"])},
            map: map
        });

        marker.addListener('click', function() {
            var str="<div style='padding:10px;'><p style='font-weight: 400;font-size:30px' >"+movie['title']+"("+movie.year+")"+"<a onclick = like() style='color:red' >   <i class='fa fa-heart' aria-hidden='true'></i></a></p>"
                    +"<img class='col-sm-6' src='"+movie.poster+"' alt='Mountain View' style='width:auto;height:160px;margin-bottom: 20px'>"
                    +"<div style='font-weight: 400'>Rating: <span style='font-weight: 200'>"+movie.idbrating+"</span></div>"

                    +"<div style='font-weight: 400'>Genre: <span style='font-weight: 200'>"+movie.genre+"</span></div>"

                    +"<div style='font-weight: 400'>Location: <span style='font-weight: 200'>"+movie.address+"</span></div></div>"
                ;
            console.log(str);
            v = document.getElementsByClassName("markerbtn");

            document.getElementById("l0").innerHTML = movie.recom0;
            //document.getElementById("l0").onclick = move()
            document.getElementById("l1").innerHTML = movie.recom1;
            document.getElementById("l2").innerHTML = movie.recom2;
            document.getElementById("l3").innerHTML = movie.recom3;
            document.getElementById("l4").innerHTML = movie.recom4;
            document.getElementById("l5").innerHTML = movie.recom5;
            document.getElementById("l6").innerHTML = movie.recom6;
            document.getElementById("l7").innerHTML = movie.recom7;
            document.getElementById("l8").innerHTML = movie.recom8;
            document.getElementById("l9").innerHTML = movie.recom9;



            id = movie['imdbid'];


            infowindow.setContent(str);
            infowindow.open(map, marker);
        });
        markers.push(marker);
    }


        map.addListener("idle", function (event) {
            var bounds = map.getBounds();
            north = bounds.getNorthEast().lat();
            south = bounds.getSouthWest().lat();
            west = bounds.getNorthEast().lng();
            east = bounds.getSouthWest().lng();
            //boundChange();
            getData(function() {
                refresh();

            });

        });

    // Sets the map on all markers in the array.
    function refresh(){
        deleteMarkers();
        for (var i = 0; i < list.length; i++) {
            addMarker(list[i]);
        }
        showMarkers();
    }
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
        markers.length = 0;
    }
    $('#search').on('click',function () {
        var ip = document.getElementById("input");
        var temp = ip.value;
        if(ip.value == "")
            return;
        arr = ip.value.split(' ');
        $("#input").val("");
        $('#input').attr('placeholder',temp);
        var link = "";
        for(var i =0; i<arr.length;i++ ){
            link+=arr[i];
            if(i == arr.length-1)
                break;
            link+="_";
        }
        link+="/";
        console.log(link);
        //return;
        $.get("http://fa16-cs411-04.cs.illinois.edu:8000/moviefun/location/"+link, function(data, status){
            if(data.error==1)
                return;
            console.log(data[0]);
            //return;
            var northEast = new google.maps.LatLng(data[0].nelat,data[0].nelng);
            var southWest = new google.maps.LatLng(data[0].swlat,data[0].swlng);
            var bounds = new google.maps.LatLngBounds(southWest,northEast);
            map.fitBounds(bounds);
z
            north = bounds.getNorthEast().lat();
            south = bounds.getSouthWest().lat();
            west = bounds.getNorthEast().lng();
            east = bounds.getSouthWest().lng();
            //map.setCenter(new google.maps.LatLng((data.nelat+data.swlat)/2,(data.nelng+data.swlng)/2));
            getData(function(){

                //boundChange();
                refresh();
            });
            //TODO: check if trigger "idle"
        });
    });
    $('#test').on('click',function () {
        console.log("test");
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
        if(ct==7){
            genre={'Action': true,'Adventure': true,'Crime': true,'Drama': true,'Musical': true,'Romance': true,'Western':true};
        }
        getData(function(){
            refresh();
        });
    });
}

var main=function() {
    var mySidenav = document.getElementById("mySidenav");

// Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");
    //$( function() {
        $( "#slider-year" ).slider({
            range: true,
            min: 1900,
            max: 2016,
            values: [ 1900, 2016 ],
            slide: function( event, ui ) {
                $( "#year_range" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
                year[0] = ui.values[ 0 ];
                year[1] = ui.values[ 1 ];
                getData(function () {

                });
            }
        });
        $( "#year_range" ).val(  + $( "#slider-year" ).slider( "values", 0 ) +
            " - " + $( "#slider-year" ).slider( "values", 1 ) );
   // } );
    $( "#slider-rating" ).slider({
        range: true,
        min: 0.0,
        max: 10.0,
        step: 0.1,
        values: [ 0.0, 10.0 ],
        slide: function( event, ui ) {
            $( "#rating_range" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
            ratings[0] = ui.values[ 0 ];
            ratings[1] = ui.values[ 1 ];
            getData(function () {

            });
        }
    });
    $( "#rating_range" ).val(  + $( "#slider-rating" ).slider( "values", 0 ) +
        " - " + $( "#slider-rating" ).slider( "values", 1 ) );

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
    $('#ratings').on('click','input', function () {
        var filter = document.getElementById("ratings");
        var ct=0;
        for(var i = 0; i < filter.children.length; i++){
            var curr = filter.children[i].children[0];
            if(!curr.checked) ct++;
            ratings[curr.value] = curr.checked?true:false;
        }
        if(ct==7){
            ratings={'6.0': true,'7.0': true,'8.0':true};
        }
        console.log(ct);
    });
    $(".markerbtn").live('click', function(){
        console.log("enen");
    });




}
function check() {
    console.log("check");
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
    if(year[0]==undefined){
        year = [1900,2016];
    }
    if(ratings[0]==undefined){
        ratings = [0.0,10.0];
    }
    var rate0 = ratings[0].toString();
    var rate1 = ratings[1].toString();
    if(rate0.indexOf(".")==-1)
        rate0+=".0";
    if(rate1.indexOf(".")==-1)
        rate1+=".0";
    console.log(genre);
    //return;
    $.get("http://fa16-cs411-04.cs.illinois.edu:8000/moviefun/filter/"+
           (north+180.0).toString()+"/"+(south+180.0).toString()+"/"+
        (west+180.0).toString()+"/"+(east+180.0).toString()+"/"+
        year[0]+"/"+year[1]+"/"+rate0+"/"+rate1+"/"+genre['Action']+"/"+genre['Adventure']+"/"+genre['Crime']+"/"
        +genre['Drama']+"/"+genre['Musical']+"/"+genre['Romance']+"/"+genre['Western']+"/", function(data, status){
        list = data;
    });

    callback();    
}
function like(){
    console.log("in like");
    $.get("http://fa16-cs411-04.cs.illinois.edu:8000/moviefun/like/"+id+"/", function(data){
    });
}

$(document).ready(main);

var app = angular.module('movieApp',[]);
app.controller('ListCtrl', ['$scope', '$http',"$window", function($scope, $http,$window) {
    $scope.test = $window.recList;
    $scope.$watch(
        function() { return $window.recList },
        function(n,o) {
            console.log("changed ",n);
        }
    );
    $scope.$on("$routeChangeSuccess", function () {console.log("sucee")});
    $(".markerbtn").live('click', function(){
        console.log("enen");
    });
    $scope.check = function(){
        console.log("check");
    }
    var check = function() {
        console.log("out");
    }



}]);

