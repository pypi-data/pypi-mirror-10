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
    .controller("ExposuresCtrl", function($scope, $interval,
                                          riskAPI, riskReport, riskValidators){

        if (riskReport.parms.port != ""){
            riskAPI.getExposures(riskReport.parms.port, function(response){
                $scope.exposures = response;
            })
        } else {
            $scope.exposures = [];
        };

        $scope.fund = riskReport.parms.info;

        // refresh
        var promise = $interval(function(){
            riskAPI.getExposures(riskReport.parms.port, function(response){
                $scope.exposures = response;
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
                riskAPI.getExposures(newValue, function(response){
                    $scope.exposures = response;
                })
            };
        });

        // add validators
        $scope.validateGross = function(){
            if ($scope.exposures == undefined){
                return "plain";
            } else {
                value = $scope.exposures.gross / $scope.fund.aum;
                return riskValidators.baseValidator(value, 3.0);
            };
        };

        $scope.validateNet = function(){
            if ($scope.exposures == undefined){
                return "plain";
            } else {
                value = Math.abs($scope.exposures.net / $scope.fund.aum);
                return riskValidators.baseValidator(value, 0.50);
            };
        };

        $scope.validateCommod = function(){
            if ($scope.exposures == undefined){
                return "plain";
            } else {
                value = Math.abs($scope.exposures.commod / $scope.fund.aum);
                return riskValidators.baseValidator(value, 0.25);
            };
        };
    });