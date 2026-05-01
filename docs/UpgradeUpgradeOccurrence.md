# UpgradeUpgradeOccurrence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **str** |  | [optional] 
**hour** | **int** |  | [optional] 
**minute** | **int** |  | [optional] 
**occurrence_in_month** | **int** |  | [optional] 
**ordinal** | **str** |  | [optional] 
**weekday** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.upgrade_upgrade_occurrence import UpgradeUpgradeOccurrence

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeUpgradeOccurrence from a JSON string
upgrade_upgrade_occurrence_instance = UpgradeUpgradeOccurrence.from_json(json)
# print the JSON string representation of the object
print(UpgradeUpgradeOccurrence.to_json())

# convert the object into a dict
upgrade_upgrade_occurrence_dict = upgrade_upgrade_occurrence_instance.to_dict()
# create an instance of UpgradeUpgradeOccurrence from a dict
upgrade_upgrade_occurrence_from_dict = UpgradeUpgradeOccurrence.from_dict(upgrade_upgrade_occurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


