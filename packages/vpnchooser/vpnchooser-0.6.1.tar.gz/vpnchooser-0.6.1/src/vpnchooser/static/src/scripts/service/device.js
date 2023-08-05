/**
 * service/device.js
 *
 * Service to access the devices.
 */

var deviceServices = angular.module('deviceServices', ['ngResource']);

deviceServices.factory(
    'Device',
    function ($resource) {
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
    }
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
