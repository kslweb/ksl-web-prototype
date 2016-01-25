var applogin = angular.module('kslweb', ['ngRoute']);

applogin.config(function($routeProvider){
	$routeProvider
	.otherwise({
		redirectTo : '/ksl'
	});
});