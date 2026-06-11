# V1ExtranetPublicVifIdGetResponse


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
from graphiant_sdk.models.v1_extranet_public_vif_id_get_response import V1ExtranetPublicVifIdGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetPublicVifIdGetResponse from a JSON string
v1_extranet_public_vif_id_get_response_instance = V1ExtranetPublicVifIdGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetPublicVifIdGetResponse.to_json())

# convert the object into a dict
v1_extranet_public_vif_id_get_response_dict = v1_extranet_public_vif_id_get_response_instance.to_dict()
# create an instance of V1ExtranetPublicVifIdGetResponse from a dict
v1_extranet_public_vif_id_get_response_from_dict = V1ExtranetPublicVifIdGetResponse.from_dict(v1_extranet_public_vif_id_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


