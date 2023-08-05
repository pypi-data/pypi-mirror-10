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

angular.module("jobsSchedulerApp")
    .controller("EditCtrl", function($scope, $modalInstance, job){
        $scope.job = job;
        $scope.executors = ["default", "processpool"];

        $scope.upload = function(){
            $modalInstance.close($scope.job);
        };

        $scope.cancel = function(){
            $modalInstance.dismiss("cancel");
        };
    })