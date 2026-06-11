# ManaV2LanSegmentSitesMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_ids** | [**Dict[str, ManaV2SiteLanSegmentDeviceBuckets]**](ManaV2SiteLanSegmentDeviceBuckets.md) |  | [optional] 
**site_list_ids** | [**Dict[str, ManaV2SiteLanSegmentDeviceBuckets]**](ManaV2SiteLanSegmentDeviceBuckets.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_lan_segment_sites_map import ManaV2LanSegmentSitesMap

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2LanSegmentSitesMap from a JSON string
mana_v2_lan_segment_sites_map_instance = ManaV2LanSegmentSitesMap.from_json(json)
# print the JSON string representation of the object
print(ManaV2LanSegmentSitesMap.to_json())

# convert the object into a dict
mana_v2_lan_segment_sites_map_dict = mana_v2_lan_segment_sites_map_instance.to_dict()
# create an instance of ManaV2LanSegmentSitesMap from a dict
mana_v2_lan_segment_sites_map_from_dict = ManaV2LanSegmentSitesMap.from_dict(mana_v2_lan_segment_sites_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


