# V1ZtagentBindingsPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**site_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_ztagent_bindings_put_request import V1ZtagentBindingsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ZtagentBindingsPutRequest from a JSON string
v1_ztagent_bindings_put_request_instance = V1ZtagentBindingsPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1ZtagentBindingsPutRequest.to_json())

# convert the object into a dict
v1_ztagent_bindings_put_request_dict = v1_ztagent_bindings_put_request_instance.to_dict()
# create an instance of V1ZtagentBindingsPutRequest from a dict
v1_ztagent_bindings_put_request_from_dict = V1ZtagentBindingsPutRequest.from_dict(v1_ztagent_bindings_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


