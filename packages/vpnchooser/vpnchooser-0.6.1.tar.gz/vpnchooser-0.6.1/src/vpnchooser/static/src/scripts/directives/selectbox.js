/**
 * directives/selectbox.js
 *
 * Directives to render a semantic-ui select
 * box correctly.
 */

vpnChooserApp.directive('ngSelectBox', function ($timeout) {
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
        controller: function($scope, $element) {
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

        },
        templateUrl: 'src/partials/directives/select_box.html'
    }
});
