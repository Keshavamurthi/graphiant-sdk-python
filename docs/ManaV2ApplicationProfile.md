# ManaV2ApplicationProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_range** | **str** | Port Range | [optional] 
**ports** | **List[int]** |  | 
**protocol** | **int** | Protocol for the application profile (required) | 

## Example

```python
from graphiant_sdk.models.mana_v2_application_profile import ManaV2ApplicationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2ApplicationProfile from a JSON string
mana_v2_application_profile_instance = ManaV2ApplicationProfile.from_json(json)
# print the JSON string representation of the object
print(ManaV2ApplicationProfile.to_json())

# convert the object into a dict
mana_v2_application_profile_dict = mana_v2_application_profile_instance.to_dict()
# create an instance of ManaV2ApplicationProfile from a dict
mana_v2_application_profile_from_dict = ManaV2ApplicationProfile.from_dict(mana_v2_application_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


