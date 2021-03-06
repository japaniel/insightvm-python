# swagger_client.AdministrationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_license**](AdministrationApi.md#activate_license) | **POST** /api/3/administration/license | License
[**execute_command**](AdministrationApi.md#execute_command) | **POST** /api/3/administration/commands | Console Commands
[**get_info**](AdministrationApi.md#get_info) | **GET** /api/3/administration/info | Information
[**get_license**](AdministrationApi.md#get_license) | **GET** /api/3/administration/license | License
[**get_properties**](AdministrationApi.md#get_properties) | **GET** /api/3/administration/properties | Properties
[**get_settings**](AdministrationApi.md#get_settings) | **GET** /api/3/administration/settings | Settings

# **activate_license**
> Links activate_license(license=license, key=key)

License

Licenses the product with an activation key or a provided license file. If both are provided, the license file is preferred. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))
license = 'license_example' # str |  (optional)
key = 'key_example' # str | A license activation key. (optional)

try:
    # License
    api_response = api_instance.activate_license(license=license, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->activate_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license** | **str**|  | [optional] 
 **key** | **str**| A license activation key. | [optional] 

### Return type

[**Links**](Links.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_command**
> ConsoleCommandOutput execute_command(body=body)

Console Commands

Executes a console command against the Security Console. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | The console command to execute. (optional)

try:
    # Console Commands
    api_response = api_instance.execute_command(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->execute_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The console command to execute. | [optional] 

### Return type

[**ConsoleCommandOutput**](ConsoleCommandOutput.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info**
> Info get_info()

Information

Returns system details, including host and version information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))

try:
    # Information
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Info**](Info.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license**
> License get_license()

License

Returns the enabled features and limits of the current license. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))

try:
    # License
    api_response = api_instance.get_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**License**](License.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> EnvironmentProperties get_properties()

Properties

Returns system details, including host and version information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))

try:
    # Properties
    api_response = api_instance.get_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnvironmentProperties**](EnvironmentProperties.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> Settings get_settings()

Settings

Returns the current administration settings. <span class=\"authorization\">Global Administrator</span>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AdministrationApi(swagger_client.ApiClient(configuration))

try:
    # Settings
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrationApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

