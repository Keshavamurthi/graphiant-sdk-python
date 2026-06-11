# V1SitesMapDetailsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lan_segment_ids** | [**Dict[str, ManaV2LanSegmentSitesMap]**](ManaV2LanSegmentSitesMap.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_sites_map_details_get_response import V1SitesMapDetailsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1SitesMapDetailsGetResponse from a JSON string
v1_sites_map_details_get_response_instance = V1SitesMapDetailsGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1SitesMapDetailsGetResponse.to_json())

# convert the object into a dict
v1_sites_map_details_get_response_dict = v1_sites_map_details_get_response_instance.to_dict()
# create an instance of V1SitesMapDetailsGetResponse from a dict
v1_sites_map_details_get_response_from_dict = V1SitesMapDetailsGetResponse.from_dict(v1_sites_map_details_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


