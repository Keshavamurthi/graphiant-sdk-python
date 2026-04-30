# UpgradeUpgradeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** |  | [optional] 
**end_of_life** | **bool** |  | [optional] 
**last_discovered_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**last_running_version** | [**UpgradeSwVersion**](UpgradeSwVersion.md) |  | [optional] 
**last_upgrade_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**ready_for_activation_version** | [**UpgradeSwVersion**](UpgradeSwVersion.md) |  | [optional] 
**rollout_id** | **int** |  | [optional] 
**rollout_name** | **str** |  | [optional] 
**running_version** | [**UpgradeSwVersion**](UpgradeSwVersion.md) |  | [optional] 
**schedule** | [**UpgradeSchedule**](UpgradeSchedule.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_upgrade_summary import UpgradeUpgradeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeUpgradeSummary from a JSON string
upgrade_upgrade_summary_instance = UpgradeUpgradeSummary.from_json(json)
# print the JSON string representation of the object
print(UpgradeUpgradeSummary.to_json())

# convert the object into a dict
upgrade_upgrade_summary_dict = upgrade_upgrade_summary_instance.to_dict()
# create an instance of UpgradeUpgradeSummary from a dict
upgrade_upgrade_summary_from_dict = UpgradeUpgradeSummary.from_dict(upgrade_upgrade_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


