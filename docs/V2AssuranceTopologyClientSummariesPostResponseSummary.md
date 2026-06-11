# V2AssuranceTopologyClientSummariesPostResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_server_key** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**client_username** | **str** |  | [optional] 
**lan_segments** | **List[str]** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**server_site_enterprise_name** | **str** |  | [optional] 
**server_site_name** | **str** |  | [optional] 
**session_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_client_summaries_post_response_summary import V2AssuranceTopologyClientSummariesPostResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyClientSummariesPostResponseSummary from a JSON string
v2_assurance_topology_client_summaries_post_response_summary_instance = V2AssuranceTopologyClientSummariesPostResponseSummary.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyClientSummariesPostResponseSummary.to_json())

# convert the object into a dict
v2_assurance_topology_client_summaries_post_response_summary_dict = v2_assurance_topology_client_summaries_post_response_summary_instance.to_dict()
# create an instance of V2AssuranceTopologyClientSummariesPostResponseSummary from a dict
v2_assurance_topology_client_summaries_post_response_summary_from_dict = V2AssuranceTopologyClientSummariesPostResponseSummary.from_dict(v2_assurance_topology_client_summaries_post_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


