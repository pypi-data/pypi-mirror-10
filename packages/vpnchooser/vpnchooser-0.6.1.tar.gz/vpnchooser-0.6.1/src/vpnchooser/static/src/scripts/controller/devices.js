vpnChooserControllers.controller('devicesCtrl', function ($scope, Device, DeviceType) {

    $scope.devices = Device.query();

    $scope.add_device = function () {
        var newDevice = new Device();
        newDevice.type = 'pc';
        newDevice.is_new = true;
        $scope.devices.push(newDevice);
    };

});


vpnChooserControllers.controller('deviceCtrl', function ($scope, $q, $timeout, Device, DeviceType, Vpn) {
    $scope.deviceTypes = DeviceType;

    $scope.save = function () {
        var device = $scope.device;
        if ($scope.deviceForm.$valid) {
            if (!device.id) {
                Device.save(device, function (d_return) {
                    $scope.device = d_return;
                });
            } else {
                Device.update({id: device.id}, device);
            }
        }
    };

    $scope.delete = function ($event) {
        $event && $event.stopPropagation();
        var device = $scope.device;

        if (device.id) {
            Device.delete({id: device.id}, function () {
                var device_ids = $scope.devices.map(function (device) {
                    return device.id;
                });
                $scope.devices.splice(
                    device_ids.indexOf(device.id),
                    1
                );
            });
        }
    };

    $scope.vpns = Vpn.query();

});
