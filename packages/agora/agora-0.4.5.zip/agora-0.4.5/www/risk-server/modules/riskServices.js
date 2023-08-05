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

angular.module("riskServices", [])
    .factory("riskAPI", ["$http", function($http){
        return {
            getFunds: function(onSuccess){
                $http.get("http://localhost:9000/objects/Fund")
                    .success(function(response){
                        onSuccess(response);
                    })
                    .error(function(data, status, headers, config){
                        console.log(data);
                    });
            },

            getFundInfo: function(fund_name, onSuccess){
                $http.get("http://localhost:9000/fund/" + fund_name)
                    .success(function(response){
                        onSuccess(response);
                    })
                    .error(function(data, status, headers, config){
                        console.log(data);
                    });
            },

            getPositions: function(port_name, onSuccess){
                $http.get("http://localhost:9000/positions/" + port_name)
                    .success(function(response){
                        onSuccess(response);
                    })
                    .error(function(data, status, headers, config){
                        console.log(data);
                    });
            },

            getExposures: function(port_name, onSuccess){
                $http.get("http://localhost:9000/exposures/" + port_name)
                    .success(function(response){
                        onSuccess(response);
                    })
                    .error(function(data, status, headers, config){
                        console.log(data);
                    });
            },

            getGrossAttributions: function(port_name, onSuccess){
                $http.get("http://localhost:9000/gross_attributions/" + port_name)
                    .success(function(response){
                        onSuccess(response);
                    })
                    .error(function(data, status, headers, config){
                        console.log(data);
                    });
            },

            getStressScenarios: function(port_name, onSuccess){
                $http.get("http://localhost:9000/stress/" + port_name)
                    .success(function(response){
                        onSuccess(response);
                    })
                    .error(function(data, status, headers, config){
                        console.log(data);
                    });
            },

        };
    }])

    .factory("riskReport", function(){
        var parms = {
            date: new Date(),
            fund: "",
            port: "",
            info: {},
        };

        return {
            setDate: function(date){ parms.date = date; },
            setFund: function(fund){ parms.fund = fund; },
            setPort: function(port){ parms.port = port; },
            parms: parms,
        };
    })

    .factory("riskValidators", function(){
        // base validator: sets warnings at 80%, 90% and 100% of the set limit
        function baseValidator(value, limit){
            if (value > 1.0*limit){ return "limit-breached"; };
            if (value > 0.9*limit){ return "hard-warning"; };
            if (value > 0.8*limit){ return "soft-warning"; };
            return "plain";
        };

        return {
            baseValidator: baseValidator,
            validateWeight: function(w){ return baseValidator(Math.abs(w), 0.15); },
            validateDays: function(days){ return baseValidator(days, 5.0); },
        };
    });
