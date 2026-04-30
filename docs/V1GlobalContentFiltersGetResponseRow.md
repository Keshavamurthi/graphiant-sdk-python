# V1GlobalContentFiltersGetResponseRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**global_content_filter_id** | **int** | ID for the global content filter. | [optional] 
**global_content_filter_name** | **str** | Given name of this global content filter. | [optional] 
**lans** | [**List[V1GlobalContentFiltersGetResponseRowLanEntry]**](V1GlobalContentFiltersGetResponseRowLanEntry.md) |  | [optional] 
**rules** | [**List[V1GlobalContentFiltersGetResponseRowRuleEntry]**](V1GlobalContentFiltersGetResponseRowRuleEntry.md) |  | [optional] 
**sites** | [**List[V1GlobalContentFiltersGetResponseRowSiteEntry]**](V1GlobalContentFiltersGetResponseRowSiteEntry.md) |  | [optional] 
**updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_content_filters_get_response_row import V1GlobalContentFiltersGetResponseRow

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalContentFiltersGetResponseRow from a JSON string
v1_global_content_filters_get_response_row_instance = V1GlobalContentFiltersGetResponseRow.from_json(json)
# print the JSON string representation of the object
print(V1GlobalContentFiltersGetResponseRow.to_json())

# convert the object into a dict
v1_global_content_filters_get_response_row_dict = v1_global_content_filters_get_response_row_instance.to_dict()
# create an instance of V1GlobalContentFiltersGetResponseRow from a dict
v1_global_content_filters_get_response_row_from_dict = V1GlobalContentFiltersGetResponseRow.from_dict(v1_global_content_filters_get_response_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


