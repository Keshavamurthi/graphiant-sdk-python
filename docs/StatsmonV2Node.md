# StatsmonV2Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit_info** | [**List[StatsmonV2NodeCircuitInfo]**](StatsmonV2NodeCircuitInfo.md) |  | [optional] 
**connections** | [**List[StatsmonV2NodeConnection]**](StatsmonV2NodeConnection.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**node_info** | [**StatsmonV2NodeDeviceInfo**](StatsmonV2NodeDeviceInfo.md) |  | [optional] 
**preferred_region_name** | **str** |  | [optional] 
**quality** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.statsmon_v2_node import StatsmonV2Node

# TODO update the JSON string below
json = "{}"
# create an instance of StatsmonV2Node from a JSON string
statsmon_v2_node_instance = StatsmonV2Node.from_json(json)
# print the JSON string representation of the object
print(StatsmonV2Node.to_json())

# convert the object into a dict
statsmon_v2_node_dict = statsmon_v2_node_instance.to_dict()
# create an instance of StatsmonV2Node from a dict
statsmon_v2_node_from_dict = StatsmonV2Node.from_dict(statsmon_v2_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


