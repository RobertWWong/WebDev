var app = angular.module('servin', []);

//we are creating a service called sumMessages
app.controller('ListCtrl', ['$scope', 'message', function($scope,message){

	$scope.array = message.list;

	$scope.update = function (msg){
		message.add(msg);
	};
}]);




app.factory('message', ['', function(){
	var someObj = {};

	someObj.list = [];

	someObj.add = function (msg){
		someObj.list.push(msg);
	};

	return someObj;
}]);

