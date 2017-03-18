/**
 * AngularJS Tutorial 1
 * @author Nick Kaye <nick.c.kaye@gmail.com>
 */

/**
 * Main AngularJS Web Application
 */
var app = angular.module('aioquiz', [
  'ngRoute'
]);

/**
 * Configure the Routes
 */
app.config(['$routeProvider', function ($routeProvider) {
  $routeProvider
    .when("/", {templateUrl: "partials/home.html", controller: "PageCtrl"})
    .when("/about", {templateUrl: "partials/about.html", controller: "PageCtrl"})
    .when("/live_quiz", {templateUrl: "partials/live_quiz.html", controller: "PageCtrl"})
    .when("/quiz", {templateUrl: "partials/quiz.html", controller: "PageCtrl"})
    .when("/propose", {templateUrl: "partials/propose.html", controller: "PageCtrl"})
    .when("/review", {templateUrl: "partials/review.html", controller: "PageCtrl"})
    .when("/create_quiz", {templateUrl: "partials/create_quiz.html", controller: "PageCtrl"})
    .when("/login", {templateUrl: "partials/login.html", controller: "PageCtrl"})
    .when("/register", {templateUrl: "partials/register.html", controller: "PageCtrl"})
    .when("/profile", {templateUrl: "partials/profile.html", controller: "PageCtrl"})
    .when("/admin", {templateUrl: "partials/admin.html", controller: "PageCtrl"})
    .otherwise("/404", {templateUrl: "partials/404.html", controller: "PageCtrl"});
}]);


/**
 * Controls all other Pages
 */
app.controller('PageCtrl', function (/* $scope, $location, $http */) {
  console.log("Page Controller reporting for duty.");

  // Activates the Carousel
  $('.carousel').carousel({
    interval: 5000
  });

  // Activates Tooltips for Social Links
  $('.tooltip-social').tooltip({
    selector: "a[data-toggle=tooltip]"
  })
});