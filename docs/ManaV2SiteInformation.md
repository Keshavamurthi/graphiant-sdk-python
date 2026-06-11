# ManaV2SiteInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_lists** | **List[int]** |  | [optional] 
**sites** | **List[int]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.mana_v2_site_information import ManaV2SiteInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ManaV2SiteInformation from a JSON string
mana_v2_site_information_instance = ManaV2SiteInformation.from_json(json)
# print the JSON string representation of the object
print(ManaV2SiteInformation.to_json())

# convert the object into a dict
mana_v2_site_information_dict = mana_v2_site_information_instance.to_dict()
# create an instance of ManaV2SiteInformation from a dict
mana_v2_site_information_from_dict = ManaV2SiteInformation.from_dict(mana_v2_site_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


