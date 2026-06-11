# ManaV2PublicVifConsumerLanSegmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_prefixes** | **List[str]** |  | [optional] 
**outbound_security_rules** | [**List[ManaV2SecurityPolicyRule]**](ManaV2SecurityPolicyRule.md) |  | [optional] 
**service_lan_segment** | **int** | LAN segment ID for the service | [optional] 
**traffic_rules** | [**List[ManaV2TrafficPolicyRule]**](ManaV2TrafficPolicyRule.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_consumer_lan_segment_response import ManaV2PublicVifConsumerLanSegmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifConsumerLanSegmentResponse from a JSON string
mana_v2_public_vif_consumer_lan_segment_response_instance = ManaV2PublicVifConsumerLanSegmentResponse.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifConsumerLanSegmentResponse.to_json())

# convert the object into a dict
mana_v2_public_vif_consumer_lan_segment_response_dict = mana_v2_public_vif_consumer_lan_segment_response_instance.to_dict()
# create an instance of ManaV2PublicVifConsumerLanSegmentResponse from a dict
mana_v2_public_vif_consumer_lan_segment_response_from_dict = ManaV2PublicVifConsumerLanSegmentResponse.from_dict(mana_v2_public_vif_consumer_lan_segment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


