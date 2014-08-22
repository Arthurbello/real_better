var theapp = angular.module('myApp', ['ng', 'ngCookies']);

theapp.run(function($rootScope, $http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
});

theapp.controller("myController", function($scope, $http, $location, $timeout, $window) {

    $scope.sub = function() {
    $timeout(function() {
        $window.location.href = 'http://127.0.0.1:8000/';

}, 3000);};

    $scope.submitter = function() {
    $scope.snow = true;
    $scope.life= true;
      $scope.sun = false;
    }
    ;
    $scope.submitterer = function() {
    $scope.sun = true;
    $scope.rain = true
    }
    ;
    $scope.submit = function() {
//        console.log($scope.rome);
        // This is not very DRY, these all look exactly the same, minus the choice you're using
        // Could turn this into a function which loops through and makes all of these POSTs
        $http({
            method: "post",
            url: '/api/v1/rainfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.rainchoice1
            }
        });
        $http({
            method: "post",
            url: '/api/v1/rainfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.rainchoice2
            }
        });
        $http({
            method: "post",
            url: '/api/v1/rainfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.rainchoice3
            }
        });
        if ($scope.rainchoice4) {
            $http({
            method: "post",
            url: '/api/v1/rainfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.rainchoice4
            }
        });
        }
        if ($scope.rainchoice5) {
            $http({
            method: "post",
            url: '/api/v1/rainfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.rainchoice5
            }
        });
        }
        $http({
            method: "post",
            url: '/api/v1/sunfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.sunchoice1
            }
        });
        $http({
            method: "post",
            url: '/api/v1/sunfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.sunchoice2
            }
        });
        $http({
            method: "post",
            url: '/api/v1/sunfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.sunchoice3
            }
        });
        if ($scope.sunchoice4) {
            $http({
                method: "post",
                url: '/api/v1/sunfavourite/',
                headers: {'Content-Type': 'application/json;'},
                data: {
//                user: $scope.username,
                    choice: $scope.sunchoice4
                }
            });
        }
        if ($scope.sunchoice5) {
            $http({
                method: "post",
                url: '/api/v1/sunfavourite/',
                headers: {'Content-Type': 'application/json;'},
                data: {
//                user: $scope.username,
                    choice: $scope.sunchoice5
                }
            });
        }
        $http({
            method: "post",
            url: '/api/v1/snowfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.snowchoice1
            }
        });
        $http({
            method: "post",
            url: '/api/v1/snowfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.snowchoice2
            }
        });
        $http({
            method: "post",
            url: '/api/v1/snowfavourite/',
            headers : {'Content-Type':'application/json;'},
            data: {
//                user: $scope.username,
                choice: $scope.snowchoice3
            }
        });
        if ($scope.sunchoice4) {
            $http({
                method: "post",
                url: '/api/v1/snowfavourite/',
                headers: {'Content-Type': 'application/json;'},
                data: {
//                user: $scope.username,
                    choice: $scope.snowchoice4
                }
            });
        }
        if ($scope.sunchoice5) {
            $http({
                method: "post",
                url: '/api/v1/snowfavourite/',
                headers: {'Content-Type': 'application/json;'},
                data: {
//                user: $scope.username,
                    choice: $scope.snowchoice5
                }
            });
        }
    };

});





