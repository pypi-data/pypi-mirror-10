vpnChooserControllers.controller('vpnsCtrl', function ($scope, Vpn, UserService) {

    $scope.vpns = Vpn.query();
    $scope.user_service = UserService;

    $scope.add_vpn = function () {
        var newVpn = new Vpn();
        $scope.vpns.push(newVpn);
    };

    Object.defineProperty($scope, 'disabled', {
        get: function() {
            return !UserService.is_admin;
        }
    });

});

vpnChooserControllers.controller('vpnCtrl', function ($scope, $timeout, Vpn, UserService) {

    $scope.save = function () {
        var vpn = $scope.vpn;
        if ($scope.vpnForm.$valid) {
            if (!vpn.id) {
                Vpn.save(vpn, function (vpn_return) {
                    $scope.vpn = vpn_return;
                });
            } else {
                Vpn.update({id: vpn.id}, vpn);
            }
        }
    };

    $scope.delete = function ($event) {
        $event && $event.stopPropagation();
        var vpn = $scope.vpn;

        if (vpn.id) {
            Vpn.delete({id: vpn.id}, function () {
                var vpn_ids = $scope.vpns.map(function (vpn) {
                    return vpn.id
                });
                $scope.devices.splice(
                    vpn_ids.indexOf(vpn.id),
                    1
                );
            });
        }
    };

    $scope.disabled = function() {
        return !$scope.is_admin;
    };

    $scope.displayDeleteButton = function() {
        return $scope.vpn.id && $scope.is_admin;
    };

    Object.defineProperty($scope, 'is_admin', {
        get: function() {
            return UserService.is_admin;
        }
    });

});
