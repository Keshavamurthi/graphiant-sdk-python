# ManaV2PublicVifSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id of this Public VIF | [optional] 
**service_name** | **str** | name of this Public VIF | [optional] 
**updated_at** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**user_name** | **str** | creator of this Public VIF | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_public_vif_summary import ManaV2PublicVifSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2PublicVifSummary from a JSON string
mana_v2_public_vif_summary_instance = ManaV2PublicVifSummary.from_json(json)
# print the JSON string representation of the object
print(ManaV2PublicVifSummary.to_json())

# convert the object into a dict
mana_v2_public_vif_summary_dict = mana_v2_public_vif_summary_instance.to_dict()
# create an instance of ManaV2PublicVifSummary from a dict
mana_v2_public_vif_summary_from_dict = ManaV2PublicVifSummary.from_dict(mana_v2_public_vif_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


