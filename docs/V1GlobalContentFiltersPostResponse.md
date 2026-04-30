# V1GlobalContentFiltersPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_content_filter_id** | **int** | Server-assigned ID for the newly created global content filter. | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_content_filters_post_response import V1GlobalContentFiltersPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalContentFiltersPostResponse from a JSON string
v1_global_content_filters_post_response_instance = V1GlobalContentFiltersPostResponse.from_json(json)
# print the JSON string representation of the object
print(V1GlobalContentFiltersPostResponse.to_json())

# convert the object into a dict
v1_global_content_filters_post_response_dict = v1_global_content_filters_post_response_instance.to_dict()
# create an instance of V1GlobalContentFiltersPostResponse from a dict
v1_global_content_filters_post_response_from_dict = V1GlobalContentFiltersPostResponse.from_dict(v1_global_content_filters_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


