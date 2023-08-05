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
    .controller("ReportCtrl", function($scope, riskAPI, riskReport){

        riskAPI.getFunds(function(response){
            $scope.funds = response;
            $scope.fundSelected = riskReport.parms.fund = $scope.funds[0];
        })

        $scope.$watch("fundSelected", function(newValue, oldValue){
            if (newValue !== oldValue){
                riskReport.setFund(newValue);

                riskAPI.getFundInfo(newValue, function(response){
                    $scope.info = riskReport.parms.info = response;
                    $scope.portSelected = riskReport.parms.port = $scope.info.portfolios[0];
                })
            };
        });

        $scope.$watch("portSelected", function(newValue, oldValue){
            if (newValue !== oldValue){
                riskReport.setPort(newValue);
            };
        });

        $scope.dateSelected = riskReport.parms.date;

        $scope.$watch("dateSelected", function(newValue, oldValue){
            if (newValue !== oldValue){
                riskReport.setDate(newValue);
            };
        });

        $scope.openCalendar = function($event){
            $event.preventDefault();
            $event.stopPropagation();
            $scope.opened = true;
        };
    });