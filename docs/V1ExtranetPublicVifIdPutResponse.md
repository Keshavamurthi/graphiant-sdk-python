# V1ExtranetPublicVifIdPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_policy** | [**ManaV2PublicVifConsumerPolicyResponse**](ManaV2PublicVifConsumerPolicyResponse.md) |  | [optional] 
**id** | **int** |  | [optional] 
**producer_policy** | [**ManaV2PublicVifProducerPolicyResponse**](ManaV2PublicVifProducerPolicyResponse.md) |  | [optional] 
**service_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_public_vif_id_put_response import V1ExtranetPublicVifIdPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetPublicVifIdPutResponse from a JSON string
v1_extranet_public_vif_id_put_response_instance = V1ExtranetPublicVifIdPutResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetPublicVifIdPutResponse.to_json())

# convert the object into a dict
v1_extranet_public_vif_id_put_response_dict = v1_extranet_public_vif_id_put_response_instance.to_dict()
# create an instance of V1ExtranetPublicVifIdPutResponse from a dict
v1_extranet_public_vif_id_put_response_from_dict = V1ExtranetPublicVifIdPutResponse.from_dict(v1_extranet_public_vif_id_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


