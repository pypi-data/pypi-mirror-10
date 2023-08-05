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
    .controller("StressCtrl", function($scope,  $interval, riskAPI, riskReport){

        function set_from_response(response){
            $scope.positions = response.positions;
            $scope.scenarios = response.scenarios;
            var length = 2*$scope.scenarios.length;
            $scope.range = Array.apply(null, Array(length)).map(function(x, i){ return i; })
        };

        if (riskReport.parms.port != ""){
            riskAPI.getStressScenarios(riskReport.parms.port, set_from_response)
        } else {
            $scope.positions = [];
            $scope.scenarios = [];
            $scope.range = [];
        };

        $scope.fund = riskReport.parms.info;

        // refresh
        var promise = $interval(function(){
            riskAPI.getStressScenarios(riskReport.parms.port, function(response){
                set_from_response(response);
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
                riskAPI.getStressScenarios(newValue, set_from_response)
            };
        });

        $scope.get_change = function(pos, i){
            if ($scope.scenarios.length > 0){
                return 100.0*pos[$scope.scenarios[Math.floor(i / 2)].name].change;
            };
        };

        $scope.get_pnl = function(pos, i){
            if ($scope.scenarios.length > 0){
                return 100.0*pos[$scope.scenarios[Math.floor(i / 2)].name].pnl;
            };
        };

        $scope.totalPnL = function(scenario){
            var total = 0.0;
            $scope.positions.forEach(function(pos){
                total += pos[scenario.name].pnl;
            });
            return total;
        };

    });