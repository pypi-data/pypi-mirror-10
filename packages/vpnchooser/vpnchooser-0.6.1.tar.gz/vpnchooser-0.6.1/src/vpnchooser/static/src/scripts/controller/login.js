vpnChooserControllers.controller('loginCtrl', function ($scope, $location, UserService) {

    var redirectToLastUsed = function() {
        $location.path('/');
    };

    UserService.isAuthenticated().then(function() {
        redirectToLastUsed();
    });

    $scope.login = function () {
        UserService
            .login($scope.user_name, $scope.password)
            .then(function () {
                redirectToLastUsed();
            }).catch(function () {
                $scope.login_form.$setValidity('', false);
            })
        ;
    }

});
