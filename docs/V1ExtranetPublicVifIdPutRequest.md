# V1ExtranetPublicVifIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_policy** | [**ManaV2PublicVifConsumerPolicy**](ManaV2PublicVifConsumerPolicy.md) |  | [optional] 
**producer_policy** | [**ManaV2PublicVifProducerPolicy**](ManaV2PublicVifProducerPolicy.md) |  | 

## Example

```python
from graphiant_sdk.models.v1_extranet_public_vif_id_put_request import V1ExtranetPublicVifIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetPublicVifIdPutRequest from a JSON string
v1_extranet_public_vif_id_put_request_instance = V1ExtranetPublicVifIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetPublicVifIdPutRequest.to_json())

# convert the object into a dict
v1_extranet_public_vif_id_put_request_dict = v1_extranet_public_vif_id_put_request_instance.to_dict()
# create an instance of V1ExtranetPublicVifIdPutRequest from a dict
v1_extranet_public_vif_id_put_request_from_dict = V1ExtranetPublicVifIdPutRequest.from_dict(v1_extranet_public_vif_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


