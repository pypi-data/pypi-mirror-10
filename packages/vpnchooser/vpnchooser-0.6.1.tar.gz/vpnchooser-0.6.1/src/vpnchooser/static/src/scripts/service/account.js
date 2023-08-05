var userService = angular.module('UserService', ['base64', 'LocalStorageModule']);

userService.factory('UserService', function ($http, $q, $base64, localStorageService) {

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

});
