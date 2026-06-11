# V1ExtranetPublicVifGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**List[ManaV2PublicVifSummary]**](ManaV2PublicVifSummary.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_extranet_public_vif_get_response import V1ExtranetPublicVifGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExtranetPublicVifGetResponse from a JSON string
v1_extranet_public_vif_get_response_instance = V1ExtranetPublicVifGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1ExtranetPublicVifGetResponse.to_json())

# convert the object into a dict
v1_extranet_public_vif_get_response_dict = v1_extranet_public_vif_get_response_instance.to_dict()
# create an instance of V1ExtranetPublicVifGetResponse from a dict
v1_extranet_public_vif_get_response_from_dict = V1ExtranetPublicVifGetResponse.from_dict(v1_extranet_public_vif_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


