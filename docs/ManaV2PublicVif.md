# ManaV2PublicVif


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**covering_prefixes** | [**ManaV2PublicVifDynamic**](ManaV2PublicVifDynamic.md) |  | 
**fixed_prefixes** | [**ManaV2PublicVifFixed**](ManaV2PublicVifFixed.md) |  | 
**type** | **str** | Type of Public VIF dynamic/fixed (required) | 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif import ManaV2PublicVif

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVif from a JSON string
mana_v2_public_vif_instance = ManaV2PublicVif.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVif.to_json())

# convert the object into a dict
mana_v2_public_vif_dict = mana_v2_public_vif_instance.to_dict()
# create an instance of ManaV2PublicVif from a dict
mana_v2_public_vif_from_dict = ManaV2PublicVif.from_dict(mana_v2_public_vif_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


