# SearchEdgeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_on** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**canary_mode** | **str** |  | [optional] 
**connected_regions** | **List[str]** |  | [optional] 
**device_id** | **int** |  | [optional] 
**discovered_location** | **str** |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 
**first_appeared_on** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**ip_detected** | **str** |  | [optional] 
**is_hardware** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] 
**is_requested** | **bool** |  | [optional] 
**last_booted_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**location** | [**ManaV2Location**](ManaV2Location.md) |  | [optional] 
**model** | **str** |  | [optional] 
**override_region** | **str** |  | [optional] 
**parent_enterprise_name** | **str** |  | [optional] 
**portal_status** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**serial_num** | **str** |  | [optional] 
**site** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**stale** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**sw_name** | **str** |  | [optional] 
**sw_version** | **str** |  | [optional] 
**tt_conn_count** | **int** |  | [optional] 
**upgrade_summary** | [**UpgradeUpgradeSummary**](UpgradeUpgradeSummary.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.search_edge_summary import SearchEdgeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEdgeSummary from a JSON string
search_edge_summary_instance = SearchEdgeSummary.from_json(json)
# print the JSON string representation of the object
print(SearchEdgeSummary.to_json())

# convert the object into a dict
search_edge_summary_dict = search_edge_summary_instance.to_dict()
# create an instance of SearchEdgeSummary from a dict
search_edge_summary_from_dict = SearchEdgeSummary.from_dict(search_edge_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


