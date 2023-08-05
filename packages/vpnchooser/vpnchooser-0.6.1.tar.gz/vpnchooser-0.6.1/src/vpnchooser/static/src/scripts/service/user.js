/**
 * service/user.js
 *
 * The Service to get users from the backend.
 */


var userServices = angular.module('userServices', ['ngResource']);

userServices.factory(
    'User',
    function($resource) {
        return $resource('/users/:name', {}, {
            query: {
                method: 'GET',
                params:{

                } ,
                isArray: true
            },
            'update': { method:'PUT' }
        });
    }
);
