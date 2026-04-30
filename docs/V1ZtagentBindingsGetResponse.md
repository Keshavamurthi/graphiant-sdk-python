# V1ZtagentBindingsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_ztagent_bindings_get_response import V1ZtagentBindingsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ZtagentBindingsGetResponse from a JSON string
v1_ztagent_bindings_get_response_instance = V1ZtagentBindingsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ZtagentBindingsGetResponse.to_json())

# convert the object into a dict
v1_ztagent_bindings_get_response_dict = v1_ztagent_bindings_get_response_instance.to_dict()
# create an instance of V1ZtagentBindingsGetResponse from a dict
v1_ztagent_bindings_get_response_from_dict = V1ZtagentBindingsGetResponse.from_dict(v1_ztagent_bindings_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


