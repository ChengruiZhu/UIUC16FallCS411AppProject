var app = angular.module('movieApp',[]);
app.controller('ListCtrl', ['$scope', '$http', function($scope, $http) {
    $scope.movies=[
        {
            "rank": 8,
            "title": "The Good, the Bad and the Ugly",
            "rated": "Not Rated",
            "released": "23 Dec 1966",
            "runtime": "161 min",
            "genre": [
                "Western"
            ],
            "director": [
                "Sergio Leone"
            ],
            "actors": [
                "Eli Wallach",
                "Clint Eastwood",
                "Lee Van Cleef",
                "Aldo Giuffrè"
            ],
            "plot": "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
            "language": [
                "Italian"
            ],
            "country": [
                "Italy",
                "Spain",
                "West Germany",
                "USA"
            ],
            "awards": "1 win.",
            "metascore": 90,
            "imdbRating": 8.9,
            "imdbVotes": 414809,
            "imdbID": "tt0060196"
        }
    ];

}]);
