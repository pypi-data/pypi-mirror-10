
vpnChooserControllers.controller('menuCtrl', function($scope, UserService) {

    $scope.isAuthenticated = function() {
        return UserService.authenticated;
    };

    $scope.isAdmin = function() {
        return UserService.is_admin;
    }

});
