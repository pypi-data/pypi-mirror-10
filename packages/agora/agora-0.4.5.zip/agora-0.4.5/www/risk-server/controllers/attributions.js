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

var chartOptions = {
    width: 450,
    height: 250,
    chartArea: {left: 10, top: 10, width: "95%", height: "95%"},
};

angular.module("riskServerApp")
    .controller("AttributionsCtrl", function($scope, $interval, riskAPI, riskReport){

        // initialize attributions
        $scope.gross_by_region = {data: undefined, options: chartOptions};
        $scope.gross_by_sector = {data: undefined, options: chartOptions};

        function set_from_response(response){
            for (var key in response){
                if (response.hasOwnProperty(key)){
                    $scope[key].data = new google.visualization.DataTable(response[key]);
                };
            };
        };

        if (riskReport.parms.port != ""){
            riskAPI.getGrossAttributions(riskReport.parms.port, set_from_response)
        };

        // refresh
        var promise = $interval(function(){
            riskAPI.getGrossAttributions(riskReport.parms.port, set_from_response);            
        }, 5*60000);

        // Cancel interval on page changes
        $scope.$on("$destroy", function(){
            if (angular.isDefined(promise)){
                $interval.cancel(promise);
                promise = undefined;
            };
        });

        // add watcher
        $scope.$watch(function(){return riskReport.parms.port;},
                      function(newValue, oldValue){
            if (newValue !== oldValue){
                riskAPI.getGrossAttributions(newValue, set_from_response);
            };
        });
    });