# UpgradeYearlyRecurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | Calendar day (1–31) for fixed month+date yearly recurrence. | [optional] 
**month** | **int** | Month of year (1–12) for yearly recurrence. (required) | 
**ordinal** | **str** | For nth-weekday-in-month yearly recurrence; use with weekday, or use month + date. | [optional] 
**weekday** | **str** | Weekday paired with ordinal for yearly recurrence. | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_yearly_recurrence import UpgradeYearlyRecurrence

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeYearlyRecurrence from a JSON string
upgrade_yearly_recurrence_instance = UpgradeYearlyRecurrence.from_json(json)
# print the JSON string representation of the object
print(UpgradeYearlyRecurrence.to_json())

# convert the object into a dict
upgrade_yearly_recurrence_dict = upgrade_yearly_recurrence_instance.to_dict()
# create an instance of UpgradeYearlyRecurrence from a dict
upgrade_yearly_recurrence_from_dict = UpgradeYearlyRecurrence.from_dict(upgrade_yearly_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


