/**
 * Snippets API
 * Test description
 *
 * OpenAPI spec version: v1
 * Contact: contact@snippets.local
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['../ApiClient', '../model/Health'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/Health'));
  } else {
    // Browser globals (root is window)
    if (!root.SnippetsApi) {
      root.SnippetsApi = {};
    }
    root.SnippetsApi.HealthcheckApi = factory(root.SnippetsApi.ApiClient, root.SnippetsApi.Health);
  }
}(this, function(ApiClient, Health) {
  'use strict';

  /**
   * Healthcheck service.
   * @module api/HealthcheckApi
   * @version v1
   */

  /**
   * Constructs a new HealthcheckApi. 
   * @alias module:api/HealthcheckApi
   * @class
   * @param {module:ApiClient} apiClient Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the healthCheckList operation.
     * @callback module:api/HealthcheckApi~healthCheckListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Health} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 
     * @param {module:api/HealthcheckApi~healthCheckListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Health}
     */
    this.healthCheckList = function(callback) {
      var postBody = null;


      var pathParams = {
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['Basic'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = Health;

      return this.apiClient.callApi(
        '/health_check', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
