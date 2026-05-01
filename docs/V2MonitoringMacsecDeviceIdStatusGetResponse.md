# V2MonitoringMacsecDeviceIdStatusGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**macsec_statuses** | [**List[V2MonitoringMacsecDeviceIdStatusGetResponseMaCsecStatus]**](V2MonitoringMacsecDeviceIdStatusGetResponseMaCsecStatus.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v2_monitoring_macsec_device_id_status_get_response import V2MonitoringMacsecDeviceIdStatusGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2MonitoringMacsecDeviceIdStatusGetResponse from a JSON string
v2_monitoring_macsec_device_id_status_get_response_instance = V2MonitoringMacsecDeviceIdStatusGetResponse.from_json(json)
# print the JSON string representation of the object
print(V2MonitoringMacsecDeviceIdStatusGetResponse.to_json())

# convert the object into a dict
v2_monitoring_macsec_device_id_status_get_response_dict = v2_monitoring_macsec_device_id_status_get_response_instance.to_dict()
# create an instance of V2MonitoringMacsecDeviceIdStatusGetResponse from a dict
v2_monitoring_macsec_device_id_status_get_response_from_dict = V2MonitoringMacsecDeviceIdStatusGetResponse.from_dict(v2_monitoring_macsec_device_id_status_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


