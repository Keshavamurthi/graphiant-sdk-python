# ManaV2ManagedEnterpriseContractInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumed_credits** | **float** | All credits consumed over the entirety the enterprise&#39;s contracts | [optional] 
**enterprise_contract** | [**CommonBillingContract**](CommonBillingContract.md) |  | [optional] 
**enterprise_id** | **int** |  | [optional] 
**enterprise_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_managed_enterprise_contract_info import ManaV2ManagedEnterpriseContractInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ManagedEnterpriseContractInfo from a JSON string
mana_v2_managed_enterprise_contract_info_instance = ManaV2ManagedEnterpriseContractInfo.from_json(json)
# print the JSON string representation of the object
print(ManaV2ManagedEnterpriseContractInfo.to_json())

# convert the object into a dict
mana_v2_managed_enterprise_contract_info_dict = mana_v2_managed_enterprise_contract_info_instance.to_dict()
# create an instance of ManaV2ManagedEnterpriseContractInfo from a dict
mana_v2_managed_enterprise_contract_info_from_dict = ManaV2ManagedEnterpriseContractInfo.from_dict(mana_v2_managed_enterprise_contract_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


