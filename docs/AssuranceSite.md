# AssuranceSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **int** |  | [optional] 
**site_enterprise_name** | **str** |  | [optional] 
**site_id** | **int** |  | [optional] 
**site_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_site import AssuranceSite

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceSite from a JSON string
assurance_site_instance = AssuranceSite.from_json(json)
# print the JSON string representation of the object
print(AssuranceSite.to_json())

# convert the object into a dict
assurance_site_dict = assurance_site_instance.to_dict()
# create an instance of AssuranceSite from a dict
assurance_site_from_dict = AssuranceSite.from_dict(assurance_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


