# ManaV2PublicVifProducerPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**Dict[str, ManaV2PublicVifDevice]**](ManaV2PublicVifDevice.md) |  | [optional] 
**inbound_security_rules** | [**List[ManaV2SecurityPolicyRule]**](ManaV2SecurityPolicyRule.md) |  | [optional] 
**profiles** | [**List[ManaV2ApplicationProfile]**](ManaV2ApplicationProfile.md) |  | [optional] 
**service_lan_segment** | **int** | LAN segment ID for the service | [optional] 
**service_name** | **str** | Public VIF service name (local_extranet_producer_service.name) | [optional] 
**sites** | [**ManaV2SiteInformation**](ManaV2SiteInformation.md) |  | [optional] 
**sla** | [**ManaV2SlaInformation**](ManaV2SlaInformation.md) |  | [optional] 
**traffic_rules** | [**List[ManaV2TrafficPolicyRule]**](ManaV2TrafficPolicyRule.md) |  | [optional] 
**vifs** | [**ManaV2PublicVif**](ManaV2PublicVif.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_producer_policy_response import ManaV2PublicVifProducerPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifProducerPolicyResponse from a JSON string
mana_v2_public_vif_producer_policy_response_instance = ManaV2PublicVifProducerPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifProducerPolicyResponse.to_json())

# convert the object into a dict
mana_v2_public_vif_producer_policy_response_dict = mana_v2_public_vif_producer_policy_response_instance.to_dict()
# create an instance of ManaV2PublicVifProducerPolicyResponse from a dict
mana_v2_public_vif_producer_policy_response_from_dict = ManaV2PublicVifProducerPolicyResponse.from_dict(mana_v2_public_vif_producer_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


