# V1SoftwareRolloutsIdGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollout** | [**UpgradeRollout**](UpgradeRollout.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_rollouts_id_get_response import V1SoftwareRolloutsIdGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareRolloutsIdGetResponse from a JSON string
v1_software_rollouts_id_get_response_instance = V1SoftwareRolloutsIdGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareRolloutsIdGetResponse.to_json())

# convert the object into a dict
v1_software_rollouts_id_get_response_dict = v1_software_rollouts_id_get_response_instance.to_dict()
# create an instance of V1SoftwareRolloutsIdGetResponse from a dict
v1_software_rollouts_id_get_response_from_dict = V1SoftwareRolloutsIdGetResponse.from_dict(v1_software_rollouts_id_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


