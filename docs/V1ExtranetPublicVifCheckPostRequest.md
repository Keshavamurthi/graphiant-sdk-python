# V1ExtranetPublicVifCheckPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer_policy** | [**ManaV2PublicVifConsumerPolicy**](ManaV2PublicVifConsumerPolicy.md) |  | 
**producer_policy** | [**ManaV2PublicVifProducerPolicy**](ManaV2PublicVifProducerPolicy.md) |  | 
**service_name** | **str** |  | [optional] 
**type** | **str** | Type of the service whether it is application or peering (required) | 

## Example

```python
from graphiant_sdk.models.v1_extranet_public_vif_check_post_request import V1ExtranetPublicVifCheckPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetPublicVifCheckPostRequest from a JSON string
v1_extranet_public_vif_check_post_request_instance = V1ExtranetPublicVifCheckPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetPublicVifCheckPostRequest.to_json())

# convert the object into a dict
v1_extranet_public_vif_check_post_request_dict = v1_extranet_public_vif_check_post_request_instance.to_dict()
# create an instance of V1ExtranetPublicVifCheckPostRequest from a dict
v1_extranet_public_vif_check_post_request_from_dict = V1ExtranetPublicVifCheckPostRequest.from_dict(v1_extranet_public_vif_check_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


