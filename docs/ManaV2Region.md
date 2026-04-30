# ManaV2Region


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**ManaV2RegionCoordinates**](ManaV2RegionCoordinates.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**region_iso_code** | **str** |  | [optional] 
**unavailable** | **bool** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_region import ManaV2Region

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2Region from a JSON string
mana_v2_region_instance = ManaV2Region.from_json(json)
# print the JSON string representation of the object
print(ManaV2Region.to_json())

# convert the object into a dict
mana_v2_region_dict = mana_v2_region_instance.to_dict()
# create an instance of ManaV2Region from a dict
mana_v2_region_from_dict = ManaV2Region.from_dict(mana_v2_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


