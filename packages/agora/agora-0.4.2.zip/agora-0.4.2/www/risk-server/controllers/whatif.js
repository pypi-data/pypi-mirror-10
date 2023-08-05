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
    .controller("WhatIfCtrl", function($scope, $http, riskReport, riskValidators){
        $scope.positions = [{ticker: "", quantity: 0}];
        $scope.report = {metrics: []}
        $scope.error_message = undefined;

        $scope.add = function(){
            $scope.positions.push({ticker: "", quantity: 0})
        };

        $scope.remove = function(i){
            $scope.positions.splice(i, 1)
        };

        $scope.run = function(){
            $scope.fund = riskReport.parms.info;
            $scope.visible = false;

            $http.post("http://localhost:9000/whatif",
                       {port: riskReport.parms.port, positions: $scope.positions},
                       {headers: {"Content-Type":
                                  "application/x-www-form-urlencoded"}})
            .success(function(response){
                $scope.report = response;
                $scope.visible = true;
                $scope.is_error = false;
            })
            .error(function(data, status, headers, config){
                console.log(data);
                $scope.visible = false;
                if (data != null){
                    $scope.error_message = data;
                    $scope.is_error = true;
                };
            });
        };

        $scope.is_error = false;
        $scope.visible = false;

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