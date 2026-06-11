# ManaV2PublicVifConsumerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan_segments** | [**List[ManaV2PublicVifConsumerLanSegment]**](ManaV2PublicVifConsumerLanSegment.md) |  | 
**sites** | [**ManaV2SiteInformation**](ManaV2SiteInformation.md) |  | 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_consumer_policy import ManaV2PublicVifConsumerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifConsumerPolicy from a JSON string
mana_v2_public_vif_consumer_policy_instance = ManaV2PublicVifConsumerPolicy.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifConsumerPolicy.to_json())

# convert the object into a dict
mana_v2_public_vif_consumer_policy_dict = mana_v2_public_vif_consumer_policy_instance.to_dict()
# create an instance of ManaV2PublicVifConsumerPolicy from a dict
mana_v2_public_vif_consumer_policy_from_dict = ManaV2PublicVifConsumerPolicy.from_dict(mana_v2_public_vif_consumer_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


