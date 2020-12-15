# Report

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bureau** | **str** | The name of the bureau for a CyberScope report. Only used when the format is &#x60;\&quot;cyberscope-xml\&quot;&#x60;. | [optional] 
**component** | **str** | The name of the component for a CyberScope report. Only used when the format is &#x60;\&quot;cyberscope-xml\&quot;&#x60;. | [optional] 
**database** | [**ReportConfigDatabaseResource**](ReportConfigDatabaseResource.md) |  | [optional] 
**email** | [**ReportEmail**](ReportEmail.md) |  | [optional] 
**enclave** | **str** | The name of the enclave for a CyberScope report. Only used when the format is &#x60;\&quot;cyberscope-xml\&quot;&#x60;. | [optional] 
**filters** | [**ReportConfigFiltersResource**](ReportConfigFiltersResource.md) |  | [optional] 
**format** | **str** | The output format of the report. The format will restrict the available templates and parameters that can be specified. | [optional] 
**frequency** | [**ReportFrequency**](ReportFrequency.md) |  | [optional] 
**id** | **int** | The identifier of the report. | [optional] 
**language** | **str** | The locale (language) in which the report is generated | [optional] 
**links** | [**list[Link]**](Link.md) | Hypermedia links to corresponding or related resources. | [optional] 
**name** | **str** | The name of the report. | [optional] 
**organization** | **str** | The organization used for a XCCDF XML report. Only used when the format is &#x60;\&quot;xccdf-xml\&quot;&#x60;. | [optional] 
**owner** | **int** | The identifier of the report owner. | [optional] 
**policy** | **int** | The policy to report on. Only used when the format is &#x60;\&quot;oval-xml\&quot;&#x60;, &#x60;\&quot;\&quot;xccdf-csv\&quot;&#x60;, or &#x60;\&quot;xccdf-xml\&quot;&#x60;. | [optional] 
**query** | **str** | SQL query to run against the Reporting Data Model. Only used when the format is &#x60;\&quot;sql-query\&quot;&#x60;. | [optional] 
**scope** | [**ReportConfigScopeResource**](ReportConfigScopeResource.md) |  | [optional] 
**storage** | [**ReportStorage**](ReportStorage.md) |  | [optional] 
**template** | **str** | The template for the report (only required if the format is templatized). | [optional] 
**timezone** | **str** | The timezone the report generates in, such as &#x60;\&quot;America/Los_Angeles\&quot;&#x60;. | [optional] 
**users** | **list[int]** | The identifiers of the users granted explicit access to the report. | [optional] 
**version** | **str** | The version of the report Data Model to report against. Only used when the format is &#x60;\&quot;sql-query\&quot;&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

