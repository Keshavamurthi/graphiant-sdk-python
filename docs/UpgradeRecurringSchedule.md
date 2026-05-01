# UpgradeRecurringSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly** | [**UpgradeMonthlyRecurrence**](UpgradeMonthlyRecurrence.md) |  | [optional] 
**starts_at_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | 
**weekly** | [**UpgradeWeeklyRecurrence**](UpgradeWeeklyRecurrence.md) |  | [optional] 
**yearly** | [**UpgradeYearlyRecurrence**](UpgradeYearlyRecurrence.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_recurring_schedule import UpgradeRecurringSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeRecurringSchedule from a JSON string
upgrade_recurring_schedule_instance = UpgradeRecurringSchedule.from_json(json)
# print the JSON string representation of the object
print(UpgradeRecurringSchedule.to_json())

# convert the object into a dict
upgrade_recurring_schedule_dict = upgrade_recurring_schedule_instance.to_dict()
# create an instance of UpgradeRecurringSchedule from a dict
upgrade_recurring_schedule_from_dict = UpgradeRecurringSchedule.from_dict(upgrade_recurring_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


