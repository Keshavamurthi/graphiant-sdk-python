# StatsmonV2NodeCircuitInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_downlink_utilization** | **float** |  | [optional] 
**average_uplink_utilization** | **float** |  | [optional] 
**circuit_carrier** | **str** |  | [optional] 
**circuit_name** | **str** |  | [optional] 
**connected_region_name** | **str** |  | [optional] 
**current_downlink_utilization** | **float** |  | [optional] 
**current_uplink_utilization** | **float** |  | [optional] 
**device_id** | **int** |  | [optional] 
**interface_name** | **str** |  | [optional] 
**jitter** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**last_resort** | **bool** |  | [optional] 
**latency** | **int** |  | [optional] 
**loss** | **float** |  | [optional] 
**qoe** | **float** |  | [optional] 
**quality** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.statsmon_v2_node_circuit_info import StatsmonV2NodeCircuitInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StatsmonV2NodeCircuitInfo from a JSON string
statsmon_v2_node_circuit_info_instance = StatsmonV2NodeCircuitInfo.from_json(json)
# print the JSON string representation of the object
print(StatsmonV2NodeCircuitInfo.to_json())

# convert the object into a dict
statsmon_v2_node_circuit_info_dict = statsmon_v2_node_circuit_info_instance.to_dict()
# create an instance of StatsmonV2NodeCircuitInfo from a dict
statsmon_v2_node_circuit_info_from_dict = StatsmonV2NodeCircuitInfo.from_dict(statsmon_v2_node_circuit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


