# ManaV2DomainCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional longer text describing what sites or traffic belong in this category. | [optional] 
**id** | **int** | Stable identifier for this domain category in the content-filter catalog. | [optional] 
**name** | **str** | Human-readable name of the domain category. | [optional] 
**type** | **str** | Optional category classifier or grouping hint from the catalog (e.g. vendor-specific type). | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_domain_category import ManaV2DomainCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2DomainCategory from a JSON string
mana_v2_domain_category_instance = ManaV2DomainCategory.from_json(json)
# print the JSON string representation of the object
print(ManaV2DomainCategory.to_json())

# convert the object into a dict
mana_v2_domain_category_dict = mana_v2_domain_category_instance.to_dict()
# create an instance of ManaV2DomainCategory from a dict
mana_v2_domain_category_from_dict = ManaV2DomainCategory.from_dict(mana_v2_domain_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


