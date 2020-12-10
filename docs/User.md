# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**CreateAuthenticationSource**](CreateAuthenticationSource.md) |  | [optional] 
**email** | **str** | The email address of the user. | [optional] 
**enabled** | **bool** | Whether the user account is enabled. Defaults to &#x60;true&#x60;. | [optional] 
**id** | **int** | The identifier of the user. | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**locale** | [**LocalePreferences**](LocalePreferences.md) |  | [optional] 
**locked** | **bool** | Whether the user account is locked (exceeded maximum password retry attempts). | [optional] 
**login** | **str** | The login name of the user. | 
**name** | **str** | The full name of the user. | 
**password** | **str** | The password to use for the user. | 
**password_reset_on_login** | **bool** | Whether to require a reset of the user&#x27;s password upon first login. Defaults to &#x60;false&#x60;. | [optional] 
**role** | [**UserCreateRole**](UserCreateRole.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

