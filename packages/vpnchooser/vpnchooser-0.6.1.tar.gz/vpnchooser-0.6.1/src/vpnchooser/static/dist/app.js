var userService = angular.module('UserService', ['base64', 'LocalStorageModule']);

userService.factory('UserService', ['$http', '$q', '$base64', 'localStorageService', function ($http, $q, $base64, localStorageService) {

    var userService = {
        name: null,
        api_key: null,
        is_admin: false,

        check_current: function () {
            return $http({
                method: 'GET',
                url: '/users/' + name
            });
        },

        initFromLocalStorage: function () {
            var self = this;
            if (localStorageService.isSupported) {
                var api_key = localStorageService.get('api_key'),
                    user_name = localStorageService.get('user_name')
                    ;
                if (user_name && api_key) {
                    self.setApiKey(user_name, api_key);
                }
            }
        },

        logout: function () {
            var self = this;
            if (localStorageService.isSupported) {
                localStorageService.clearAll();
            }
            self.user_name = null;
            self.api_key = null;
            self.authenticated = false;
            $http.defaults.headers.common.Authorization = null;
        },

        setApiKey: function (user_name, api_key) {
            var self = this;
            $http.defaults.headers.common.Authorization = 'Basic ' + $base64.encode(
                    user_name + ':' + api_key
            );
            if (localStorageService.isSupported) {
                localStorageService.set('user_name', user_name);
                localStorageService.set('api_key', api_key);
            }
            self.user_name = user_name;
            self.api_key = api_key;
            self.authenticated = true;
        },

        isAuthenticated: function () {
            var self = this,
                defer = $q.defer()
                ;

            if (self.user_name) {
                $http({
                    method: 'GET',
                    url: '/users/' + self.user_name
                }).success(function (data, status) {
                    if (status != 200 || !data || !data.api_key) {
                        defer.reject();
                    }
                    else {
                        self.updateWithData(data);
                        defer.resolve(data);
                    }
                });
            } else {
                defer.reject();
            }
            return defer.promise;
        },

        login: function (name, password) {
            var self = this,
                defer = $q.defer();
            self.name = name;

            $http({
                method: 'GET',
                url: '/users/' + name,
                headers: {
                    'Authorization': 'Basic ' + $base64.encode(name + ':' + password)
                }
            }).success(function (data, status) {
                if (status != 200 || !data || !data.api_key) {
                    defer.reject();
                }
                self.updateWithData(data);
                defer.resolve();

            }).error(function () {
                self.logout();
                defer.reject();
            });

            return defer.promise;
        },

        updateWithData: function(data) {
            var self = this;
            if(!data) {
                return;
            }
            self.is_admin = data.is_admin;
            self.setApiKey(data.name, data.api_key);
        },

        changePassword: function (oldPassword, newPassword) {
            var self = this
                ;

            return self._changePassword(
                self.user_name,
                newPassword,
                {
                    'Authorization': 'Basic ' + $base64.encode(name + ':' + oldPassword)
                }
            );
        },

        changePasswordAdmin: function(name, password) {
            return this._changePassword(name, password);
        },

        _changePassword: function(name, password, headers) {
            var self = this
                ;
            headers = headers || {};
            return $http({
                method: 'PUT',
                url: '/users/' + name,
                headers: headers,
                data: {
                    password: password
                }
            }).success(function(data) {
                self.updateWithData(data);
                return data;
            });
        }
    };

    userService.initFromLocalStorage();
    return userService;

}]);

/**
 * service/device.js
 *
 * Service to access the devices.
 */

var deviceServices = angular.module('deviceServices', ['ngResource']);

deviceServices.factory(
    'Device',
    ['$resource', function ($resource) {
        return $resource('/devices/:id', {}, {
            query: {
                method: 'GET',
                params: {
                    'id': ''
                },
                isArray: true
            },
            'update': { method:'PUT' }
        });
    }]
);

deviceServices.factory(
    'DeviceType',
    function () {
        return [
            {
                key: 'pc',
                name: 'Computer'
            },
            {
                key: 'notebook',
                name: 'Notebook'
            },
            {
                key: 'smartphone',
                name: 'Smartphone'
            },
            {
                key: 'tablet',
                name: 'Tablet'
            },
            {
                key: 'chromecast',
                name: 'Chromecast'
            }
        ]
    }
)

/**
 * service/user.js
 *
 * The Service to get users from the backend.
 */


var userServices = angular.module('userServices', ['ngResource']);

userServices.factory(
    'User',
    ['$resource', function($resource) {
        return $resource('/users/:name', {}, {
            query: {
                method: 'GET',
                params:{

                } ,
                isArray: true
            },
            'update': { method:'PUT' }
        });
    }]
);

/**
 * service/vpn.js
 *
 * The Service to get vpns from the backend.
 */


var vpnServices = angular.module('vpnServices', ['ngResource']);

vpnServices.factory(
    'Vpn',
    ['$resource', function($resource) {
        var vpnResource = $resource('/vpns/:id', {}, {
            query: {
                method: 'GET',
                params:{

                } ,
                isArray: true
            },
            'update': { method:'PUT' }
        });

        Object.defineProperty(
            vpnResource.prototype,
            'vpn_id',
            {
                get: function() {
                    var self = this,
                        vpn_id = /^.*\/([0-9]+)\/?$/.exec(self.vpn)

                    ;
                    return vpn_id ? parseNumeric(vpn_id[1]) : null;
                },
                set: function(value) {
                    var self = this;
                }
            }
        );

        return vpnResource;
    }]
);

/**
 * app.js
 *
 * Application javascript controller for base angular.
 */

var vpnChooserApp = angular.module('vpnChooserApp', [
    'vpnChooserControllers',
    'ui.router',
    'base64',
    'ngResource',
    'LocalStorageModule',
    'angular-loading-bar'
]);


vpnChooserApp.config(['$stateProvider', '$urlRouterProvider', '$resourceProvider', 'localStorageServiceProvider', function ($stateProvider, $urlRouterProvider, $resourceProvider, localStorageServiceProvider) {

    localStorageServiceProvider.setPrefix('scnet.vpnchooser');

    $resourceProvider.defaults.stripTrailingSlashes = false;

    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('index', {
            url: '/',
            controller: 'indexCtrl'
        })
        .state('login', {
            url: '/login',
            templateUrl: 'src/partials/login.html',
            controller: 'loginCtrl'
        })
        .state('vpnList', {
            url: '/vpns',
            templateUrl: 'src/partials/vpns.html',
            controller: 'vpnsCtrl'
        })
        .state('deviceList', {
            url: '/devices',
            templateUrl: 'src/partials/devices.html',
            controller: 'devicesCtrl'
        }).state('logout', {
            url: '/logout',
            controller: 'logoutCtrl'
        }).state('account', {
            url: '/account',
            templateUrl: 'src/partials/account.html',
            controller: 'accountCtrl'
        }).state('users', {
            url: '/users',
            templateUrl: 'src/partials/users.html',
            controller: 'usersCtrl'
        }).state('userChangePassword', {
            url: '/users/:userName/change-password',
            templateUrl: 'src/partials/users/change_password.html',
            controller: 'userCtrl'
        }).state('userNew', {
            url: '/users/new',
            templateUrl: 'src/partials/users/new.html',
            controller: 'newUserCtrl'
        }).state('userEdit', {
            url: '/users/:userName/edit',
            templateUrl: 'src/partials/users/edit.html',
            controller: 'editUserCtrl'
        })
    ;
}]).config(['$httpProvider', function ($httpProvider) {

     var interceptor = ['$rootScope', '$q', '$location', function (scope, $q, $location) {

        function success(response) {
            return response;
        }

        function error(response) {
            var status = response.status;

            if (status == 401) {
                if (!/\/users\/.*$/.exec(response.config.url) && response.config.method != "PUT") {
                    console.log("Response Error 401", response);
                    $location.path('/login').search('returnTo', $location.path());
                }
            }
            // otherwise
            return $q.reject(response);

        }

        return {
            response: success,
            responseError: error
        }

    }];
    $httpProvider.interceptors.push(interceptor);
}])
    .run(['UserService', function (UserService) {
        UserService.isAuthenticated();
    }]);

/**
 * directives/checkbox.js
 *
 * Directives to render a semantic-ui checkbox
 * correctly.
 */

vpnChooserApp.directive('ngCheckBox', ['$timeout', function ($timeout) {
    return {
        restrict: 'AE',
        require: '^ngModel ^ngDescription ^ngChange',
        template: '',
        scope: {
            model: '=ngModel',
            ngDescription: '@',
            checked: '@',
            ngChange: '&'
        },
        replace: true,
        controller: ['$scope', '$element', function($scope, $element) {
            if ($scope.checked == 'false' || $scope.checked == undefined) {
                $scope.checked = false;
            } else {
                $scope.checked = true;
                element.children()[0].setAttribute('checked', 'true');
            }

            $element.bind('click', function() {
                $scope.$apply(function() {
                    if ($scope.checked == true) {
                        $scope.checked = false;
                        $scope.model = false;
                        $element.children()[0].removeAttribute('checked');
                    } else {
                        $scope.checked = true;
                        $scope.model = true;
                        $element.children()[0].setAttribute('checked', 'true');
                    }
                    $timeout(function() {
                        $scope.ngChange();
                    }, 1);
                });
            });

            $scope.$watch('checked', function(val){
                if (val == undefined)
                    return;

                if (val == true){
                    $scope.model = true;
                    $element.children()[0].setAttribute('checked', 'true');
                } else {
                    $scope.model = false;
                    $element.children()[0].removeAttribute('checked');
                }
            });

            $scope.$watch('model', function(val) {
                if (val == undefined)
                    return;

                if (val == true){
                    $scope.checked = true;
                    $element.children()[0].setAttribute('checked', 'true');
                } else {
                    $scope.checked = false;
                    $element.children()[0].removeAttribute('checked');
                }
            });

        }],
        templateUrl: 'src/partials/directives/checkbox.html'
    }
}]);

/**
 * directives/selectbox.js
 *
 * Directives to render a semantic-ui select
 * box correctly.
 */

vpnChooserApp.directive('ngSelectBox', ['$timeout', function ($timeout) {
    return {
        restrict: 'AE',
        require: '^ngModel ^ngName ^ngCollection ^ngCollectionKey ngCollectionText',
        template: '',
        scope: {
            ngModel: '=',
            ngName: '@',
            ngCollection: '=',
            ngCollectionKey: '@',
            ngCollectionText: '@',
            ngCollectionDefaultText: '@',
            ngNullName: '@',
            ngChoose: '&'
        },
        replace: true,
        controller: ['$scope', '$element', function($scope, $element) {
            Object.defineProperty($scope, 'selectedText', {
                get: function() {
                    var typeKey = $scope.ngModel,
                        selectedItems = $scope.ngCollection.filter(
                            function (item) {
                                return item[$scope.ngCollectionKey] == typeKey;
                            }
                        );
                    if(selectedItems.length) {
                        return selectedItems[0][$scope.ngCollectionText];
                    }
                    else {
                        return $scope.ngCollectionDefaultText || '';
                    }
                }
            });

            Object.defineProperty($scope, 'showEmptyOption', {
                get: function() {
                    if($scope.ngNullName) {
                        return true;
                    } else {
                        return false;
                    }
                }
            });

            $scope.selectItem = function(option) {
                var newKey = option && option.key;
                if($scope.ngModel != newKey) {
                    $scope.ngModel = newKey;
                    $scope.selected = option ? option.value : -1;
                    $timeout(function() {
                        $scope.ngChoose && $scope.ngChoose(newKey);
                    });
                }
            };

            $timeout(function() {
                $element.dropdown();
                $scope.$watchCollection('ngCollection', function() {
                    $timeout(function() {
                        $element.dropdown();
                    }, 1);
                });
            });

            $scope.selected = -1;
            var update_collection = function() {
                var options = $scope.options = [];
                $scope.optionsLookup = {};
                $scope.ngCollection.forEach(function(item, index) {
                    var option = {
                        value: index + 1,
                        text: item[$scope.ngCollectionText],
                        key: item[$scope.ngCollectionKey]
                    };
                    options.push(option);

                    $scope.optionsLookup[option.key] = option;
                    if($scope.ngModel == option.key) {
                        $scope.selected = option.value;
                    }
                });
            };

            $scope.$watchCollection('ngCollection', update_collection);
            update_collection();

        }],
        templateUrl: 'src/partials/directives/select_box.html'
    }
}]);


var vpnChooserControllers = angular.module(
    'vpnChooserControllers',
    [
        'UserService',
        'userServices',
        'deviceServices',
        'vpnServices'
    ]
);

vpnChooserControllers.controller('accountCtrl', ['$scope', '$timeout', 'UserService', function ($scope, $timeout, UserService) {

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

}]);


vpnChooserControllers.controller('devicesCtrl', ['$scope', 'Device', 'DeviceType', function ($scope, Device, DeviceType) {

    $scope.devices = Device.query();

    $scope.add_device = function () {
        var newDevice = new Device();
        newDevice.type = 'pc';
        newDevice.is_new = true;
        $scope.devices.push(newDevice);
    };

}]);


vpnChooserControllers.controller('deviceCtrl', ['$scope', '$q', '$timeout', 'Device', 'DeviceType', 'Vpn', function ($scope, $q, $timeout, Device, DeviceType, Vpn) {
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

}]);


vpnChooserControllers.controller('indexCtrl', ['$location', '$scope', 'UserService', function($location, $scope, UserService) {
    $scope.login_required = false;
    UserService.check_current().success(function() {
        // Pass
        $location.path('/devices');
    }).error(function() {
        // Rendering login.
        $scope.login_required = true;
        $location.path('/login');
    });
}]);

vpnChooserControllers.controller('loginCtrl', ['$scope', '$location', 'UserService', function ($scope, $location, UserService) {

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

}]);

vpnChooserControllers.controller('logoutCtrl', ['$scope', '$location', 'UserService', function ($scope, $location, UserService) {
    UserService.logout();
    $location.path('/login');
}]);


vpnChooserControllers.controller('menuCtrl', ['$scope', 'UserService', function($scope, UserService) {

    $scope.isAuthenticated = function() {
        return UserService.authenticated;
    };

    $scope.isAdmin = function() {
        return UserService.is_admin;
    }

}]);

vpnChooserControllers.controller('usersCtrl', ['$scope', '$location', 'User', 'UserService', function ($scope, $location, User, UserService) {

    $scope.user_service = UserService;
    if(!UserService.is_admin) {
        $location.path('/');
        return;
    }

    $scope.users = User.query();

    $scope.moveToNew = function() {
        $location.path('/users/new');
    }

}]);

vpnChooserControllers.controller('userCtrl', ['$scope', '$location', '$stateParams', '$timeout', 'User', 'UserService', function($scope, $location, $stateParams, $timeout, User, UserService) {

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

}]);

vpnChooserControllers.controller('newUserCtrl', ['$scope', '$location', '$timeout', '$stateParams', 'User', function($scope, $location, $timeout, $stateParams, User) {

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
}]);

vpnChooserControllers.controller('editUserCtrl', ['$scope', '$location', '$timeout', '$stateParams', 'User', function($scope, $location, $timeout, $stateParams, User) {
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
}]);

vpnChooserControllers.controller('vpnsCtrl', ['$scope', 'Vpn', 'UserService', function ($scope, Vpn, UserService) {

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

}]);

vpnChooserControllers.controller('vpnCtrl', ['$scope', '$timeout', 'Vpn', 'UserService', function ($scope, $timeout, Vpn, UserService) {

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

}]);
