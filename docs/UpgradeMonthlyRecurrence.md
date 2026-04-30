# UpgradeMonthlyRecurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | Calendar day of month (1–31) for fixed-date monthly recurrence; optional if ordinal and weekday are set. | [optional] 
**ordinal** | **str** | For nth-weekday-of-month style recurrence; use together with weekday, or use date instead. | [optional] 
**weekday** | **str** | Weekday paired with ordinal for monthly nth-weekday recurrence; optional if date is set. | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_monthly_recurrence import UpgradeMonthlyRecurrence

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeMonthlyRecurrence from a JSON string
upgrade_monthly_recurrence_instance = UpgradeMonthlyRecurrence.from_json(json)
# print the JSON string representation of the object
print(UpgradeMonthlyRecurrence.to_json())

# convert the object into a dict
upgrade_monthly_recurrence_dict = upgrade_monthly_recurrence_instance.to_dict()
# create an instance of UpgradeMonthlyRecurrence from a dict
upgrade_monthly_recurrence_from_dict = UpgradeMonthlyRecurrence.from_dict(upgrade_monthly_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


