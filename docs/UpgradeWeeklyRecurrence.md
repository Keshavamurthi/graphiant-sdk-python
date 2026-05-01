# UpgradeWeeklyRecurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | Which occurrence of the weekday in the month applies for weekly-style recurrence (1–52, aligned with schedule validation). (required) | 
**weekday** | **str** | Day of week for the weekly recurrence. (required) | 

## Example

```python
from graphiant_sdk.models.upgrade_weekly_recurrence import UpgradeWeeklyRecurrence

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeWeeklyRecurrence from a JSON string
upgrade_weekly_recurrence_instance = UpgradeWeeklyRecurrence.from_json(json)
# print the JSON string representation of the object
print(UpgradeWeeklyRecurrence.to_json())

# convert the object into a dict
upgrade_weekly_recurrence_dict = upgrade_weekly_recurrence_instance.to_dict()
# create an instance of UpgradeWeeklyRecurrence from a dict
upgrade_weekly_recurrence_from_dict = UpgradeWeeklyRecurrence.from_dict(upgrade_weekly_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


