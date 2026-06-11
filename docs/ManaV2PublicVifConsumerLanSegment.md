# ManaV2PublicVifConsumerLanSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_prefixes** | **List[str]** |  | 
**service_lan_segment** | **int** | LAN segment ID for the service (required) | 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_consumer_lan_segment import ManaV2PublicVifConsumerLanSegment

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifConsumerLanSegment from a JSON string
mana_v2_public_vif_consumer_lan_segment_instance = ManaV2PublicVifConsumerLanSegment.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifConsumerLanSegment.to_json())

# convert the object into a dict
mana_v2_public_vif_consumer_lan_segment_dict = mana_v2_public_vif_consumer_lan_segment_instance.to_dict()
# create an instance of ManaV2PublicVifConsumerLanSegment from a dict
mana_v2_public_vif_consumer_lan_segment_from_dict = ManaV2PublicVifConsumerLanSegment.from_dict(mana_v2_public_vif_consumer_lan_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


