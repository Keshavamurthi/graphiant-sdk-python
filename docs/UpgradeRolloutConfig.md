# UpgradeRolloutConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Upgrade action to perform (e.g. install+activate, install only, activate, auto-upgrade). (required) | 
**description** | **str** | Optional longer description of the rollout. | [optional] 
**device_ids** | **List[int]** |  | [optional] 
**name** | **str** | Human-readable rollout name unique within the enterprise. (required) | 
**release** | **str** | Target software release for devices in this rollout. (required) | 
**schedule** | [**UpgradeRecurringSchedule**](UpgradeRecurringSchedule.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_rollout_config import UpgradeRolloutConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeRolloutConfig from a JSON string
upgrade_rollout_config_instance = UpgradeRolloutConfig.from_json(json)
# print the JSON string representation of the object
print(UpgradeRolloutConfig.to_json())

# convert the object into a dict
upgrade_rollout_config_dict = upgrade_rollout_config_instance.to_dict()
# create an instance of UpgradeRolloutConfig from a dict
upgrade_rollout_config_from_dict = UpgradeRolloutConfig.from_dict(upgrade_rollout_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


