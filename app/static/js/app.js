'use strict';

var flaskAngular = angular.module('flaskAngular', [
 'ngRoute',
]);

flaskAngular.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/index.html',
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);
