# ManaV2GlobalContentFilterRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_category_id** | **int** | ID of the category whose traffic will be blocked by the content filter. | [optional] 
**exception_wildcards** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_global_content_filter_rule import ManaV2GlobalContentFilterRule

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2GlobalContentFilterRule from a JSON string
mana_v2_global_content_filter_rule_instance = ManaV2GlobalContentFilterRule.from_json(json)
# print the JSON string representation of the object
print(ManaV2GlobalContentFilterRule.to_json())

# convert the object into a dict
mana_v2_global_content_filter_rule_dict = mana_v2_global_content_filter_rule_instance.to_dict()
# create an instance of ManaV2GlobalContentFilterRule from a dict
mana_v2_global_content_filter_rule_from_dict = ManaV2GlobalContentFilterRule.from_dict(mana_v2_global_content_filter_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


