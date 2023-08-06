angular.module('bangoo.content.edit', ['codehouse.ui'], function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
})
.controller('BangooContentEditController', ['$http', '$element', '$scope', function($http, $element, $scope){
    var self = this;
    this.url = $element.attr('action');

    $scope.isSaving = false;
    $scope.data = {};
    $scope.errors = {};

    $http.get(this.url).success(function(data){
        $scope.data = data;
    });

    this.submit = function(e){
        $scope.isSaving = true;

        e.preventDefault();
        $http({
            method: 'POST',
            url: self.url,
            data: $scope.data,
            xsrfHeaderName: 'X-CSRFToken',
            xsrfCookieName: 'csrftoken'
        }).success(function(){
            $scope.isSaving = false;
            $('.top-right').notify({
                type: 'success',
                message: { text: 'Content updated!' },
                fadeOut: { enabled: true, delay: 5000 }
            }).show();
            $scope.errors = {};
        }).error(function(retval, status, headers, config){
            $scope.isSaving = false;
            if(status !== 500){
                $scope.errors = retval;
            }
            else {
                $('.top-right').notify({
                    type: 'danger',
                    message: {text: 'Unexpected error happened!'},
                    fadeOut: {enabled: true, delay: 5000}
                }).show();
            }
        });
    }
}]);