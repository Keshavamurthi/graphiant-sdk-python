# ManaV2PublicVifProducerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**Dict[str, ManaV2PublicVifDevice]**](ManaV2PublicVifDevice.md) |  | 
**profiles** | [**List[ManaV2ApplicationProfile]**](ManaV2ApplicationProfile.md) |  | [optional] 
**service_lan_segment** | **int** | LAN segment ID for the service (required) | 
**service_name** | **str** | Public VIF service name (local_extranet_producer_service.name) | [optional] 
**sites** | [**ManaV2SiteInformation**](ManaV2SiteInformation.md) |  | 
**sla** | [**ManaV2SlaInformation**](ManaV2SlaInformation.md) |  | [optional] 
**vifs** | [**ManaV2PublicVif**](ManaV2PublicVif.md) |  | 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_producer_policy import ManaV2PublicVifProducerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifProducerPolicy from a JSON string
mana_v2_public_vif_producer_policy_instance = ManaV2PublicVifProducerPolicy.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifProducerPolicy.to_json())

# convert the object into a dict
mana_v2_public_vif_producer_policy_dict = mana_v2_public_vif_producer_policy_instance.to_dict()
# create an instance of ManaV2PublicVifProducerPolicy from a dict
mana_v2_public_vif_producer_policy_from_dict = ManaV2PublicVifProducerPolicy.from_dict(mana_v2_public_vif_producer_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


