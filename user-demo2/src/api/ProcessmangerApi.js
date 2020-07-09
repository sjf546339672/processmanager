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
    define(['../ApiClient', '../model/Hello'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/Hello'));
  } else {
    // Browser globals (root is window)
    if (!root.SnippetsApi) {
      root.SnippetsApi = {};
    }
    root.SnippetsApi.ProcessmangerApi = factory(root.SnippetsApi.ApiClient, root.SnippetsApi.Hello);
  }
}(this, function(ApiClient, Hello) {
  'use strict';

  /**
   * Processmanger service.
   * @module api/ProcessmangerApi
   * @version v1
   */

  /**
   * Constructs a new ProcessmangerApi. 
   * @alias module:api/ProcessmangerApi
   * @class
   * @param {module:ApiClient} apiClient Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the processmangerFrontapiV1HelloList operation.
     * @callback module:api/ProcessmangerApi~processmangerFrontapiV1HelloListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Hello} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 
     * @param {module:api/ProcessmangerApi~processmangerFrontapiV1HelloListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Hello}
     */
    this.processmangerFrontapiV1HelloList = function(callback) {
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
      var returnType = Hello;

      return this.apiClient.callApi(
        '/processmanger/frontapi/v1/hello/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the processmangerFrontapiV1QueryOSList operation.
     * @callback module:api/ProcessmangerApi~processmangerFrontapiV1QueryOSListCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 
     * @param {module:api/ProcessmangerApi~processmangerFrontapiV1QueryOSListCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.processmangerFrontapiV1QueryOSList = function(callback) {
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
      var returnType = null;

      return this.apiClient.callApi(
        '/processmanger/frontapi/v1/queryOS/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the processmangerFrontapiV1Read operation.
     * @callback module:api/ProcessmangerApi~processmangerFrontapiV1ReadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 
     * @param {String} agentId 
     * @param {module:api/ProcessmangerApi~processmangerFrontapiV1ReadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    this.processmangerFrontapiV1Read = function(agentId, callback) {
      var postBody = null;

      // verify the required parameter 'agentId' is set
      if (agentId == undefined || agentId == null) {
        throw "Missing the required parameter 'agentId' when calling processmangerFrontapiV1Read";
      }


      var pathParams = {
        'agent_id': agentId
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
      var returnType = null;

      return this.apiClient.callApi(
        '/processmanger/frontapi/v1/{agent_id}/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the processmangerFrontapiV1Read_0 operation.
     * @callback module:api/ProcessmangerApi~processmangerFrontapiV1Read_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * 
     * @param {String} agentId 
     * @param {String} pid 
     * @param {module:api/ProcessmangerApi~processmangerFrontapiV1Read_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    this.processmangerFrontapiV1Read_0 = function(agentId, pid, callback) {
      var postBody = null;

      // verify the required parameter 'agentId' is set
      if (agentId == undefined || agentId == null) {
        throw "Missing the required parameter 'agentId' when calling processmangerFrontapiV1Read_0";
      }

      // verify the required parameter 'pid' is set
      if (pid == undefined || pid == null) {
        throw "Missing the required parameter 'pid' when calling processmangerFrontapiV1Read_0";
      }


      var pathParams = {
        'agent_id': agentId,
        'pid': pid
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
      var returnType = null;

      return this.apiClient.callApi(
        '/processmanger/frontapi/v1/{agent_id}/{pid}/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
