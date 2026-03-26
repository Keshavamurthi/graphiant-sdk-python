# ManaV2SakConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipher_suite** | **str** |  | [optional] 
**lag_member_interface_id** | **int** | The interface ID (required for when each lag member has a different MACsec configuration - when split_sak_config_by_lag_member is true) (required) | [optional] 
**nullable_rekey_interval** | [**ManaV2NullableMaCsecRekeyInterval**](ManaV2NullableMaCsecRekeyInterval.md) |  | [optional] 
**nullable_replay_protection_window_size** | [**ManaV2NullableMaCsecReplayProtectionWindowSize**](ManaV2NullableMaCsecReplayProtectionWindowSize.md) |  | [optional] 
**rekey_interval** | **int** |  | [optional] 
**replay_protection_window_size** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_sak_configuration import ManaV2SakConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2SakConfiguration from a JSON string
mana_v2_sak_configuration_instance = ManaV2SakConfiguration.from_json(json)
# print the JSON string representation of the object
print(ManaV2SakConfiguration.to_json())

# convert the object into a dict
mana_v2_sak_configuration_dict = mana_v2_sak_configuration_instance.to_dict()
# create an instance of ManaV2SakConfiguration from a dict
mana_v2_sak_configuration_from_dict = ManaV2SakConfiguration.from_dict(mana_v2_sak_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


