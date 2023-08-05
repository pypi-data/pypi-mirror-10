/**
 * service/vpn.js
 *
 * The Service to get vpns from the backend.
 */


var vpnServices = angular.module('vpnServices', ['ngResource']);

vpnServices.factory(
    'Vpn',
    function($resource) {
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
    }
);
