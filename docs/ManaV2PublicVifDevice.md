# ManaV2PublicVifDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_burst_size** | **int** | Maximum Burst size per device (required) | 
**consumer_bw_site** | **int** | Maximum Bandwidth allocation per device (required) | 
**nat_pools** | **List[str]** |  | 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_device import ManaV2PublicVifDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifDevice from a JSON string
mana_v2_public_vif_device_instance = ManaV2PublicVifDevice.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifDevice.to_json())

# convert the object into a dict
mana_v2_public_vif_device_dict = mana_v2_public_vif_device_instance.to_dict()
# create an instance of ManaV2PublicVifDevice from a dict
mana_v2_public_vif_device_from_dict = ManaV2PublicVifDevice.from_dict(mana_v2_public_vif_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


