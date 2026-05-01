# V1SoftwareRolloutsSchedulePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_only** | **bool** | When true, only devices previously marked failed are rescheduled. | [optional] 
**id** | **int** | Rollout identifier to schedule. (required) | 
**ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_rollouts_schedule_post_request import V1SoftwareRolloutsSchedulePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareRolloutsSchedulePostRequest from a JSON string
v1_software_rollouts_schedule_post_request_instance = V1SoftwareRolloutsSchedulePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareRolloutsSchedulePostRequest.to_json())

# convert the object into a dict
v1_software_rollouts_schedule_post_request_dict = v1_software_rollouts_schedule_post_request_instance.to_dict()
# create an instance of V1SoftwareRolloutsSchedulePostRequest from a dict
v1_software_rollouts_schedule_post_request_from_dict = V1SoftwareRolloutsSchedulePostRequest.from_dict(v1_software_rollouts_schedule_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


