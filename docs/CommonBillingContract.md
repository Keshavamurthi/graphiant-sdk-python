# CommonBillingContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracted_credits** | **float** | Number of credits agreed upon for the entirety of the current contract | [optional] 
**expiration_date** | [**CommonBillingTimePeriod**](CommonBillingTimePeriod.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.common_billing_contract import CommonBillingContract

# TODO update the JSON string below
json = "{}"
# create an instance of CommonBillingContract from a JSON string
common_billing_contract_instance = CommonBillingContract.from_json(json)
# print the JSON string representation of the object
print(CommonBillingContract.to_json())

# convert the object into a dict
common_billing_contract_dict = common_billing_contract_instance.to_dict()
# create an instance of CommonBillingContract from a dict
common_billing_contract_from_dict = CommonBillingContract.from_dict(common_billing_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


