# SnippetsApi.ProcessmangerApi

All URIs are relative to *http://127.0.0.1:9005/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**processmangerFrontapiV1HelloList**](ProcessmangerApi.md#processmangerFrontapiV1HelloList) | **GET** /processmanger/frontapi/v1/hello/ | 
[**processmangerFrontapiV1QueryOSList**](ProcessmangerApi.md#processmangerFrontapiV1QueryOSList) | **GET** /processmanger/frontapi/v1/queryOS/ | 
[**processmangerFrontapiV1Read**](ProcessmangerApi.md#processmangerFrontapiV1Read) | **GET** /processmanger/frontapi/v1/{agent_id}/ | 
[**processmangerFrontapiV1Read_0**](ProcessmangerApi.md#processmangerFrontapiV1Read_0) | **GET** /processmanger/frontapi/v1/{agent_id}/{pid}/ | 


<a name="processmangerFrontapiV1HelloList"></a>
# **processmangerFrontapiV1HelloList**
> Hello processmangerFrontapiV1HelloList()





### Example
```javascript
var SnippetsApi = require('snippets_api');
var defaultClient = SnippetsApi.ApiClient.default;

// Configure HTTP basic authorization: Basic
var Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

var apiInstance = new SnippetsApi.ProcessmangerApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.processmangerFrontapiV1HelloList(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Hello**](Hello.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="processmangerFrontapiV1QueryOSList"></a>
# **processmangerFrontapiV1QueryOSList**
> processmangerFrontapiV1QueryOSList()





### Example
```javascript
var SnippetsApi = require('snippets_api');
var defaultClient = SnippetsApi.ApiClient.default;

// Configure HTTP basic authorization: Basic
var Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

var apiInstance = new SnippetsApi.ProcessmangerApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.processmangerFrontapiV1QueryOSList(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="processmangerFrontapiV1Read"></a>
# **processmangerFrontapiV1Read**
> processmangerFrontapiV1Read(agentId)





### Example
```javascript
var SnippetsApi = require('snippets_api');
var defaultClient = SnippetsApi.ApiClient.default;

// Configure HTTP basic authorization: Basic
var Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

var apiInstance = new SnippetsApi.ProcessmangerApi();

var agentId = "agentId_example"; // String | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.processmangerFrontapiV1Read(agentId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="processmangerFrontapiV1Read_0"></a>
# **processmangerFrontapiV1Read_0**
> processmangerFrontapiV1Read_0(agentId, pid)





### Example
```javascript
var SnippetsApi = require('snippets_api');
var defaultClient = SnippetsApi.ApiClient.default;

// Configure HTTP basic authorization: Basic
var Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

var apiInstance = new SnippetsApi.ProcessmangerApi();

var agentId = "agentId_example"; // String | 

var pid = "pid_example"; // String | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.processmangerFrontapiV1Read_0(agentId, pid, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentId** | **String**|  | 
 **pid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

