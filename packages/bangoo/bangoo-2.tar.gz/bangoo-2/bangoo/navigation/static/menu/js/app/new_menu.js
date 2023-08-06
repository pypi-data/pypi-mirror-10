angular.module('bangoo.navigation', ["codehouse.ui"], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('MenuController', ['$scope', '$http', function($scope, $http){
    $scope.showModal = false;

    this.callback = function(data){
        window.location = data.id + '/';
    };

    $scope.initModal = function(url){
        $http.get(url).success(function(data){
            $('#newMenuForm').data('action', url);
            angular.element($('#newMenuForm')).scope().reset(data);
            $scope.showModal = !$scope.showModal;
        });
    };
}])
.controller('NewMenuController', ['$http', '$scope', '$element', function($http, $scope, $element){
    $scope.isSaving = false;
    $scope.url = $($element).data('url');

    $scope.data = {};
    $scope.errors = {};

    $scope.reset = function(obj){
        $scope.data = obj;
        $scope.errors = {};
    };

    this.save = function(fn){
        $scope.isSaving = true;
        var url = $($element).data('action');

        $http({
            method: 'POST',
            url: url,
            data: $scope.data,
            xsrfHeaderName: 'X-CSRFToken',
            xsrfCookieName: 'csrftoken'
        }).error(function(retval, status, headers, config){
            $scope.isSaving = false;
            $scope.errors = retval;
        }).success(function(retval){
            fn(retval);
        });
    };
}]);