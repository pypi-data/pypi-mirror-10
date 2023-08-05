vpnChooserControllers.controller('usersCtrl', function ($scope, $location, User, UserService) {

    $scope.user_service = UserService;
    if(!UserService.is_admin) {
        $location.path('/');
        return;
    }

    $scope.users = User.query();

    $scope.moveToNew = function() {
        $location.path('/users/new');
    }

});

vpnChooserControllers.controller('userCtrl', function($scope, $location, $stateParams, $timeout, User, UserService) {

    if($stateParams.userName) {
        User.get({
            name: $stateParams.userName
        }, function(user) {
            $scope.user = user;
        });
    }

    $scope.moveToEdit = function() {
        $location.path('/users/' + $scope.user.name + '/edit');
    }

    $scope.checkDelete = function() {
        $scope.deleteCheck = true;
    }
    $scope.deleteDeny = function() {
        $scope.deleteCheck = false;
    }
    $scope.delete = function() {
        $scope.deleteDeny();
        $scope.user.$remove({
            name: $scope.user.name
        }).then(function() {
            var index = $scope.users.indexOf($scope.user);
            if(index !== -1) {
                $scope.users.splice(index, 1);
            }
        });
    }

});

vpnChooserControllers.controller('newUserCtrl', function($scope, $location, $timeout, $stateParams, User) {

    var user = $scope.user = new User();
    $scope.verify = function() {
        if(!user.name) {
            $scope.error = {
                header: 'Name missing',
                text: 'A name is required for the user.',
                timeout: $timeout(function() {
                    $scope.error = null;
                }, 5000)
            };
            return false;
        } else if(!user.password) {
            $scope.error = {
                header: 'Password missing',
                text: 'A password is required.',
                timeout: $timeout(function() {
                    $scope.error = null;
                }, 5000)
            };
            return false;
        }
        return true;
    };

    $scope.create = function() {
        if($scope.verify()) {
            user.$save().then(function() {
                $location.path('/users');
            }, function(error) {
                var message = "";
                if(error.status == 409) {
                    message = "A user with this name already exists."
                }
                $scope.error = {
                    header: 'Could not create the user. ' + message,
                    timeout: $timeout(function() {
                        $scope.error = null;
                    }, 5000)
                }
            });
        }
    };
});

vpnChooserControllers.controller('editUserCtrl', function($scope, $location, $timeout, $stateParams, User) {
    $scope.user = User.get({
        name: $stateParams.userName
    });

    window.user = $scope.user;
    $scope.edit = function() {
        if(!$scope.user || !$scope.user.name) {
            return;
        }
        User.update({name: $scope.user.name}, $scope.user).$promise.then(function() {

            }, function() {
                $scope.error = {
                    header: 'Could not edit the user.',
                    timeout: $timeout(function() {
                        $scope.error = null;
                    }, 5000)
                }
            }
        );
    };

    $scope.changePassword = function() {
        var password = $scope.newPassword || "";
        if(!password) {
            $scope.error = {
                    header: 'Password must not be empty',
                    text: 'The password field must not be empty.',
                    timeout: $timeout(function() {
                        $scope.error = null;
                    }, 5000)
                };
            return;
        }

        $scope.error = null;
        UserService.changePasswordAdmin(
            $scope.user.name,
            password
        ).then(function() {
                $scope.message = {
                    header: 'Password successfully changed',
                    text: 'The password has been changed successfully.',
                    timeout: $timeout(function() {
                        $scope.message = null;
                    }, 5000)
                }
            }, function() {
                $scope.error = {
                    header: 'Failed when communicating with the server',
                    text: 'Could not change password. The connection ' +
                    'with the server failed.',
                    timeout: $timeout(function() {
                        $scope.error = null;
                    }, 5000)
                }
            });
    }
});
