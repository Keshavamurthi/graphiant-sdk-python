# V2AssuranceTopologyOverviewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**app_server_key** | **str** |  | [optional] 
**bucket_id** | **str** |  | [optional] 
**exchange_service_id** | **int** |  | [optional] 
**filter** | [**V2AssuranceTopologyOverviewPostRequestTopologyFilter**](V2AssuranceTopologyOverviewPostRequestTopologyFilter.md) |  | [optional] 
**flex_algo_id** | **int** |  | [optional] 
**slider_time_window** | [**AssuranceTimeWindow**](AssuranceTimeWindow.md) |  | [optional] 
**time_window** | [**AssuranceTimeWindow**](AssuranceTimeWindow.md) |  | [optional] 
**topology_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**topology_type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_assurance_topology_overview_post_request import V2AssuranceTopologyOverviewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssuranceTopologyOverviewPostRequest from a JSON string
v2_assurance_topology_overview_post_request_instance = V2AssuranceTopologyOverviewPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssuranceTopologyOverviewPostRequest.to_json())

# convert the object into a dict
v2_assurance_topology_overview_post_request_dict = v2_assurance_topology_overview_post_request_instance.to_dict()
# create an instance of V2AssuranceTopologyOverviewPostRequest from a dict
v2_assurance_topology_overview_post_request_from_dict = V2AssuranceTopologyOverviewPostRequest.from_dict(v2_assurance_topology_overview_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


