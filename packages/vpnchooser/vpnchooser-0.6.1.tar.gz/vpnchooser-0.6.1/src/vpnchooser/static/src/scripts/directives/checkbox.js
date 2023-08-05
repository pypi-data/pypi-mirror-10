/**
 * directives/checkbox.js
 *
 * Directives to render a semantic-ui checkbox
 * correctly.
 */

vpnChooserApp.directive('ngCheckBox', function ($timeout) {
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
        controller: function($scope, $element) {
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

        },
        templateUrl: 'src/partials/directives/checkbox.html'
    }
});
