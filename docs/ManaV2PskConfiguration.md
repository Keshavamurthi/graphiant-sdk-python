# ManaV2PskConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cak** | **str** | The Connection Authentication Key (CAK) | [optional] 
**cak_cryptographic_algorithm** | **str** | The cryptographic algorithm for the CAK, SAK Cipher Suite is implicitly selected based on this field. (required) | [optional] 
**ckn** | **str** | The Connection Key Name (CKN) (required) | [optional] 
**nickname** | **str** | The nickname of the PSK (required) | [optional] 
**start_time** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**use_xpn_for_cipher_suite** | **bool** | Whether to use XPN for the cipher suite. If true, AES_128_GCM_XPN or AES_256_GCM_XPN is selected based on the cmac algorithm. If false, AES_128_GCM or AES_256_GCM is selected based on the cmac algorithm. | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_psk_configuration import ManaV2PskConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PskConfiguration from a JSON string
mana_v2_psk_configuration_instance = ManaV2PskConfiguration.from_json(json)
# print the JSON string representation of the object
print(ManaV2PskConfiguration.to_json())

# convert the object into a dict
mana_v2_psk_configuration_dict = mana_v2_psk_configuration_instance.to_dict()
# create an instance of ManaV2PskConfiguration from a dict
mana_v2_psk_configuration_from_dict = ManaV2PskConfiguration.from_dict(mana_v2_psk_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


