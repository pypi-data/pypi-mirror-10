vpnChooserControllers.controller('logoutCtrl', function ($scope, $location, UserService) {
    UserService.logout();
    $location.path('/login');
});
