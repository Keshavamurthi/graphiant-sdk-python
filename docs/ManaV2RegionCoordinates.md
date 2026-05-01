# ManaV2RegionCoordinates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_region_coordinates import ManaV2RegionCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2RegionCoordinates from a JSON string
mana_v2_region_coordinates_instance = ManaV2RegionCoordinates.from_json(json)
# print the JSON string representation of the object
print(ManaV2RegionCoordinates.to_json())

# convert the object into a dict
mana_v2_region_coordinates_dict = mana_v2_region_coordinates_instance.to_dict()
# create an instance of ManaV2RegionCoordinates from a dict
mana_v2_region_coordinates_from_dict = ManaV2RegionCoordinates.from_dict(mana_v2_region_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


