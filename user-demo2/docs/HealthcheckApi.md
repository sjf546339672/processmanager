# SnippetsApi.HealthcheckApi

All URIs are relative to *http://127.0.0.1:9005/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheckList**](HealthcheckApi.md#healthCheckList) | **GET** /health_check | 


<a name="healthCheckList"></a>
# **healthCheckList**
> Health healthCheckList()





### Example
```javascript
var SnippetsApi = require('snippets_api');
var defaultClient = SnippetsApi.ApiClient.default;

// Configure HTTP basic authorization: Basic
var Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

var apiInstance = new SnippetsApi.HealthcheckApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.healthCheckList(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

