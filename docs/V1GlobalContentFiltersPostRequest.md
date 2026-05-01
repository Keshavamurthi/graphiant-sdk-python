# V1GlobalContentFiltersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**ManaV2GlobalContentFilterConfig**](ManaV2GlobalContentFilterConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_content_filters_post_request import V1GlobalContentFiltersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalContentFiltersPostRequest from a JSON string
v1_global_content_filters_post_request_instance = V1GlobalContentFiltersPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1GlobalContentFiltersPostRequest.to_json())

# convert the object into a dict
v1_global_content_filters_post_request_dict = v1_global_content_filters_post_request_instance.to_dict()
# create an instance of V1GlobalContentFiltersPostRequest from a dict
v1_global_content_filters_post_request_from_dict = V1GlobalContentFiltersPostRequest.from_dict(v1_global_content_filters_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


