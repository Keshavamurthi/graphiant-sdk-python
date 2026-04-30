# V1GlobalContentFiltersGetResponseRowRuleEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_category** | **str** | Name of the domain category whose traffic is blocked by this rule. | [optional] 
**exception_wildcards** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_content_filters_get_response_row_rule_entry import V1GlobalContentFiltersGetResponseRowRuleEntry

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalContentFiltersGetResponseRowRuleEntry from a JSON string
v1_global_content_filters_get_response_row_rule_entry_instance = V1GlobalContentFiltersGetResponseRowRuleEntry.from_json(json)
# print the JSON string representation of the object
print(V1GlobalContentFiltersGetResponseRowRuleEntry.to_json())

# convert the object into a dict
v1_global_content_filters_get_response_row_rule_entry_dict = v1_global_content_filters_get_response_row_rule_entry_instance.to_dict()
# create an instance of V1GlobalContentFiltersGetResponseRowRuleEntry from a dict
v1_global_content_filters_get_response_row_rule_entry_from_dict = V1GlobalContentFiltersGetResponseRowRuleEntry.from_dict(v1_global_content_filters_get_response_row_rule_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


