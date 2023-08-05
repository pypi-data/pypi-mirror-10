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


vpnChooserApp.config(function ($stateProvider, $urlRouterProvider, $resourceProvider, localStorageServiceProvider) {

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
}).config(function ($httpProvider) {

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
})
    .run(function (UserService) {
        UserService.isAuthenticated();
    });
