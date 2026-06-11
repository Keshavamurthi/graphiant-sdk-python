# ManaV2PublicVifConsumerPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_service_id** | **int** |  | [optional] 
**lan_segments** | [**List[ManaV2PublicVifConsumerLanSegmentResponse]**](ManaV2PublicVifConsumerLanSegmentResponse.md) |  | [optional] 
**sites** | [**ManaV2SiteInformation**](ManaV2SiteInformation.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_consumer_policy_response import ManaV2PublicVifConsumerPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifConsumerPolicyResponse from a JSON string
mana_v2_public_vif_consumer_policy_response_instance = ManaV2PublicVifConsumerPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifConsumerPolicyResponse.to_json())

# convert the object into a dict
mana_v2_public_vif_consumer_policy_response_dict = mana_v2_public_vif_consumer_policy_response_instance.to_dict()
# create an instance of ManaV2PublicVifConsumerPolicyResponse from a dict
mana_v2_public_vif_consumer_policy_response_from_dict = ManaV2PublicVifConsumerPolicyResponse.from_dict(mana_v2_public_vif_consumer_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


