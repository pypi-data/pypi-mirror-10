vpnChooserControllers.controller('accountCtrl', function ($scope, $timeout, UserService) {

    $scope.user = UserService;

    $scope.changePassword = function($event) {
        $event && $event.stopPropagation();

        var oldPassword = $scope.oldPassword,
            newPassword = $scope.newPassword
        ;

        ['message', 'error'].forEach(function(name) {
            $scope.message &&
            $scope.message[name] &&
            $timeout.cancel($scope.message[name]);
        });
        $scope.message = null;
        $scope.error = null;
        UserService.changePassword(oldPassword, newPassword)
            .success(function() {
                $scope.message = {
                    header: 'Password changed',
                    text: 'Your password has been changed successfully.',
                    timeout: $timeout(function() {
                        $scope.message = null;
                    }, 5000)
                };
                $scope.oldPassword = '';
                $scope.newPassword = '';
            })
            .catch(function() {
                $scope.error = {
                    header: 'Password change failed',
                    text: 'Could not change your password. Please verify ' +
                        'if your old one has been entered correctly.',
                    timeout: $timeout(function() {
                        $scope.error = null;
                    }, 5000)
                };
            })
        ;
        return false;
    }

});

