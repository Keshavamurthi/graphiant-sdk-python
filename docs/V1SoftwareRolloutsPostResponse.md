# V1SoftwareRolloutsPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier of the created rollout. (required) | [optional] 

## Example

```python
from graphiant_sdk.models.v1_software_rollouts_post_response import V1SoftwareRolloutsPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SoftwareRolloutsPostResponse from a JSON string
v1_software_rollouts_post_response_instance = V1SoftwareRolloutsPostResponse.from_json(json)
# print the JSON string representation of the object
print(V1SoftwareRolloutsPostResponse.to_json())

# convert the object into a dict
v1_software_rollouts_post_response_dict = v1_software_rollouts_post_response_instance.to_dict()
# create an instance of V1SoftwareRolloutsPostResponse from a dict
v1_software_rollouts_post_response_from_dict = V1SoftwareRolloutsPostResponse.from_dict(v1_software_rollouts_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


