# UpgradeRolloutDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | Device identifier. (required) | [optional] 
**hostname** | **str** | Device hostname for display. | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_rollout_device import UpgradeRolloutDevice

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeRolloutDevice from a JSON string
upgrade_rollout_device_instance = UpgradeRolloutDevice.from_json(json)
# print the JSON string representation of the object
print(UpgradeRolloutDevice.to_json())

# convert the object into a dict
upgrade_rollout_device_dict = upgrade_rollout_device_instance.to_dict()
# create an instance of UpgradeRolloutDevice from a dict
upgrade_rollout_device_from_dict = UpgradeRolloutDevice.from_dict(upgrade_rollout_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


