# CommonBillingTimePeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.common_billing_time_period import CommonBillingTimePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of CommonBillingTimePeriod from a JSON string
common_billing_time_period_instance = CommonBillingTimePeriod.from_json(json)
# print the JSON string representation of the object
print(CommonBillingTimePeriod.to_json())

# convert the object into a dict
common_billing_time_period_dict = common_billing_time_period_instance.to_dict()
# create an instance of CommonBillingTimePeriod from a dict
common_billing_time_period_from_dict = CommonBillingTimePeriod.from_dict(common_billing_time_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


