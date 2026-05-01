# V1GlobalContentFiltersGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | [**List[V1GlobalContentFiltersGetResponseRow]**](V1GlobalContentFiltersGetResponseRow.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_content_filters_get_response import V1GlobalContentFiltersGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalContentFiltersGetResponse from a JSON string
v1_global_content_filters_get_response_instance = V1GlobalContentFiltersGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1GlobalContentFiltersGetResponse.to_json())

# convert the object into a dict
v1_global_content_filters_get_response_dict = v1_global_content_filters_get_response_instance.to_dict()
# create an instance of V1GlobalContentFiltersGetResponse from a dict
v1_global_content_filters_get_response_from_dict = V1GlobalContentFiltersGetResponse.from_dict(v1_global_content_filters_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


