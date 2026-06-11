# V1MspManagedEnterpriseContractInfoGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprises** | [**List[ManaV2ManagedEnterpriseContractInfo]**](ManaV2ManagedEnterpriseContractInfo.md) |  | [optional] 
**msp_consumed_credits** | **float** | All credits consumed by the MSP over the entirety of its contracts | [optional] 
**msp_contract** | [**CommonBillingContract**](CommonBillingContract.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_msp_managed_enterprise_contract_info_get_response import V1MspManagedEnterpriseContractInfoGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1MspManagedEnterpriseContractInfoGetResponse from a JSON string
v1_msp_managed_enterprise_contract_info_get_response_instance = V1MspManagedEnterpriseContractInfoGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1MspManagedEnterpriseContractInfoGetResponse.to_json())

# convert the object into a dict
v1_msp_managed_enterprise_contract_info_get_response_dict = v1_msp_managed_enterprise_contract_info_get_response_instance.to_dict()
# create an instance of V1MspManagedEnterpriseContractInfoGetResponse from a dict
v1_msp_managed_enterprise_contract_info_get_response_from_dict = V1MspManagedEnterpriseContractInfoGetResponse.from_dict(v1_msp_managed_enterprise_contract_info_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


