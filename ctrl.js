var myapp = angular.module("deApp", []);

myapp.controller('appCtrl', ['$scope', function($scope){
	//I don't want to use this, I would have to reference all my variable as main then.
	//Not worth the extra typing
	var self = this;

	$scope.message = "Praise the Sun!";
	$scope.updateMessage = function (msg) {
		$scope.message = msg;
	}

}]);