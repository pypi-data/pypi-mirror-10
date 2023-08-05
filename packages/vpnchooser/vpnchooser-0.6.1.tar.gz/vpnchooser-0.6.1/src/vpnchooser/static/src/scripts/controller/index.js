
vpnChooserControllers.controller('indexCtrl', function($location, $scope, UserService) {
    $scope.login_required = false;
    UserService.check_current().success(function() {
        // Pass
        $location.path('/devices');
    }).error(function() {
        // Rendering login.
        $scope.login_required = true;
        $location.path('/login');
    });
});
