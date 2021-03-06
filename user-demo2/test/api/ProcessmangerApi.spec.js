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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SnippetsApi);
  }
}(this, function(expect, SnippetsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SnippetsApi.ProcessmangerApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('ProcessmangerApi', function() {
    describe('processmangerFrontapiV1HelloList', function() {
      it('should call processmangerFrontapiV1HelloList successfully', function(done) {
        //uncomment below and update the code to test processmangerFrontapiV1HelloList
        //instance.processmangerFrontapiV1HelloList(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('processmangerFrontapiV1QueryOSList', function() {
      it('should call processmangerFrontapiV1QueryOSList successfully', function(done) {
        //uncomment below and update the code to test processmangerFrontapiV1QueryOSList
        //instance.processmangerFrontapiV1QueryOSList(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('processmangerFrontapiV1Read', function() {
      it('should call processmangerFrontapiV1Read successfully', function(done) {
        //uncomment below and update the code to test processmangerFrontapiV1Read
        //instance.processmangerFrontapiV1Read(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('processmangerFrontapiV1Read_0', function() {
      it('should call processmangerFrontapiV1Read_0 successfully', function(done) {
        //uncomment below and update the code to test processmangerFrontapiV1Read_0
        //instance.processmangerFrontapiV1Read_0(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
