# SiteCredential

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | 
**description** | **str** | The description of the credential. | [optional] 
**enabled** | **bool** | Flag indicating whether the credential is enabled for use during the scan. | [optional] 
**host_restriction** | **str** | The host name or IP address that you want to restrict the credentials to. | [optional] 
**id** | **int** | The identifier of the credential. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**name** | **str** | The name of the credential. | 
**port_restriction** | **int** | Further restricts the credential to attempt to authenticate on a specific port. The port can only be restricted if the property &#x60;hostRestriction&#x60; is specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

