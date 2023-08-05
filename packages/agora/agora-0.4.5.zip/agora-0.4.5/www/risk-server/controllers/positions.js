/*#############################################################################
#
#   Agora Portfolio & Risk Management System
#
#   Copyright 2015 Carlo Sbraccia
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#############################################################################*/

angular.module("riskServerApp")
    .controller("PositionsCtrl", function($scope, $interval,
                                          riskAPI, riskReport, riskValidators){

        if (riskReport.parms.port != ""){
            riskAPI.getPositions(riskReport.parms.port, function(response){
                $scope.positions = response;
            })
        } else {
            $scope.positions = []
        };

        $scope.fund = riskReport.parms.info;

        // refresh
        var promise = $interval(function(){
            riskAPI.getPositions(riskReport.parms.port, function(response){
                $scope.positions = response;
                $scope.fund = riskReport.parms.info;
            });            
        }, 5*60000);

        // Cancel interval on page changes
        $scope.$on("$destroy", function(){
            if (angular.isDefined(promise)){
                $interval.cancel(promise);
                promise = undefined;
            };
        });

        // add watchers
        $scope.$watch(function(){return riskReport.parms.fund;},
                      function(newValue, oldValue){
            if (newValue !== oldValue){
                $scope.fund = riskReport.parms.info;
            };
        });

        $scope.$watch(function(){return riskReport.parms.port;},
                      function(newValue, oldValue){
            if (newValue !== oldValue){
                riskAPI.getPositions(newValue, function(response){
                    $scope.positions = response;
                })
            };
        });

        $scope.colorByPos = function(pos){
            if (pos < 0.0){
                return "red";
            } else {
                return "green";
            };
        };

        // add validators
        $scope.validateWeight = riskValidators.validateWeight;
        $scope.validateDays = riskValidators.validateDays;
    });