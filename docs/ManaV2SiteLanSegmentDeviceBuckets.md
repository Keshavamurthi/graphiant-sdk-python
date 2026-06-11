# ManaV2SiteLanSegmentDeviceBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan_segment_exists** | [**List[ManaV2SiteDeviceSummary]**](ManaV2SiteDeviceSummary.md) |  | [optional] 
**lan_segment_missing** | [**List[ManaV2SiteDeviceSummary]**](ManaV2SiteDeviceSummary.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_site_lan_segment_device_buckets import ManaV2SiteLanSegmentDeviceBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2SiteLanSegmentDeviceBuckets from a JSON string
mana_v2_site_lan_segment_device_buckets_instance = ManaV2SiteLanSegmentDeviceBuckets.from_json(json)
# print the JSON string representation of the object
print(ManaV2SiteLanSegmentDeviceBuckets.to_json())

# convert the object into a dict
mana_v2_site_lan_segment_device_buckets_dict = mana_v2_site_lan_segment_device_buckets_instance.to_dict()
# create an instance of ManaV2SiteLanSegmentDeviceBuckets from a dict
mana_v2_site_lan_segment_device_buckets_from_dict = ManaV2SiteLanSegmentDeviceBuckets.from_dict(mana_v2_site_lan_segment_device_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


