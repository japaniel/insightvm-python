# SyslogAlert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating the alert is enabled. | 
**enabled_scan_events** | [**ScanEvents**](ScanEvents.md) |  | [optional] 
**enabled_vulnerability_events** | [**VulnerabilityEvents**](VulnerabilityEvents.md) |  | [optional] 
**id** | **int** | The identifier of the alert. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**maximum_alerts** | **int** | The maximum number of alerts that will be issued. To disable maximum alerts, omit the property in the request or specify the property with a value of &#x60;null&#x60;. | [optional] 
**name** | **str** | The name of the alert. | 
**notification** | **str** | The type of alert. | 
**server** | **str** | The Syslog server to send messages to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

