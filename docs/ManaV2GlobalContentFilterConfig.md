# ManaV2GlobalContentFilterConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan_names** | **List[str]** |  | [optional] 
**name** | **str** | Display name for this global content filter configuration. | [optional] 
**rules** | [**List[ManaV2GlobalContentFilterRule]**](ManaV2GlobalContentFilterRule.md) |  | [optional] 
**site_list_id** | **int** | Site list whose members this content filter applies to; omit the oneof when no site scope is set. | [optional] 
**use_all_sites** | **bool** | When true, the filter applies to all sites in the tenant (must be the constant true). | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_global_content_filter_config import ManaV2GlobalContentFilterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2GlobalContentFilterConfig from a JSON string
mana_v2_global_content_filter_config_instance = ManaV2GlobalContentFilterConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2GlobalContentFilterConfig.to_json())

# convert the object into a dict
mana_v2_global_content_filter_config_dict = mana_v2_global_content_filter_config_instance.to_dict()
# create an instance of ManaV2GlobalContentFilterConfig from a dict
mana_v2_global_content_filter_config_from_dict = ManaV2GlobalContentFilterConfig.from_dict(mana_v2_global_content_filter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


