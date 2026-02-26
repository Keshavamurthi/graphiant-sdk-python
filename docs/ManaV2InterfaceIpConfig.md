# ManaV2InterfaceIpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ManaV2NullableAddress**](ManaV2NullableAddress.md) |  | [optional] 
**dhcp** | [**ManaV2InterfaceDhcpConfig**](ManaV2InterfaceDhcpConfig.md) |  | [optional] 
**gw** | [**ManaV2NullableGatewayConfig**](ManaV2NullableGatewayConfig.md) |  | [optional] 
**vrrp** | [**ManaV2NullableVrrpGroupConfig**](ManaV2NullableVrrpGroupConfig.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_interface_ip_config import ManaV2InterfaceIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2InterfaceIpConfig from a JSON string
mana_v2_interface_ip_config_instance = ManaV2InterfaceIpConfig.from_json(json)
# print the JSON string representation of the object
print(ManaV2InterfaceIpConfig.to_json())

# convert the object into a dict
mana_v2_interface_ip_config_dict = mana_v2_interface_ip_config_instance.to_dict()
# create an instance of ManaV2InterfaceIpConfig from a dict
mana_v2_interface_ip_config_from_dict = ManaV2InterfaceIpConfig.from_dict(mana_v2_interface_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


