# V1EnterpriseContractPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contracted_credits** | **float** | Amount of credits billed for a contract term or per month when no expiration is provided. For an MSP tenant, this is the total credits in the MSP billing pool (from which credits are allocated to managed enterprises). | [optional] 
**expiration_date** | [**ManaV2TimePeriod**](ManaV2TimePeriod.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_enterprise_contract_put_request import V1EnterpriseContractPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnterpriseContractPutRequest from a JSON string
v1_enterprise_contract_put_request_instance = V1EnterpriseContractPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1EnterpriseContractPutRequest.to_json())

# convert the object into a dict
v1_enterprise_contract_put_request_dict = v1_enterprise_contract_put_request_instance.to_dict()
# create an instance of V1EnterpriseContractPutRequest from a dict
v1_enterprise_contract_put_request_from_dict = V1EnterpriseContractPutRequest.from_dict(v1_enterprise_contract_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


