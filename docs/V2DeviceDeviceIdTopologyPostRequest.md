# V2DeviceDeviceIdTopologyPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_time** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**time_window** | [**StatsmonV2TimeWindow**](StatsmonV2TimeWindow.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_device_device_id_topology_post_request import V2DeviceDeviceIdTopologyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2DeviceDeviceIdTopologyPostRequest from a JSON string
v2_device_device_id_topology_post_request_instance = V2DeviceDeviceIdTopologyPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2DeviceDeviceIdTopologyPostRequest.to_json())

# convert the object into a dict
v2_device_device_id_topology_post_request_dict = v2_device_device_id_topology_post_request_instance.to_dict()
# create an instance of V2DeviceDeviceIdTopologyPostRequest from a dict
v2_device_device_id_topology_post_request_from_dict = V2DeviceDeviceIdTopologyPostRequest.from_dict(v2_device_device_id_topology_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


