# AssuranceRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **int** |  | [optional] 
**region_iso_code** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_region import AssuranceRegion

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceRegion from a JSON string
assurance_region_instance = AssuranceRegion.from_json(json)
# print the JSON string representation of the object
print(AssuranceRegion.to_json())

# convert the object into a dict
assurance_region_dict = assurance_region_instance.to_dict()
# create an instance of AssuranceRegion from a dict
assurance_region_from_dict = AssuranceRegion.from_dict(assurance_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


