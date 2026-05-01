# V1GlobalDomainCategoriesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_categories** | [**List[ManaV2DomainCategory]**](ManaV2DomainCategory.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_global_domain_categories_get_response import V1GlobalDomainCategoriesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlobalDomainCategoriesGetResponse from a JSON string
v1_global_domain_categories_get_response_instance = V1GlobalDomainCategoriesGetResponse.from_json(json)
# print the JSON string representation of the object
print(V1GlobalDomainCategoriesGetResponse.to_json())

# convert the object into a dict
v1_global_domain_categories_get_response_dict = v1_global_domain_categories_get_response_instance.to_dict()
# create an instance of V1GlobalDomainCategoriesGetResponse from a dict
v1_global_domain_categories_get_response_from_dict = V1GlobalDomainCategoriesGetResponse.from_dict(v1_global_domain_categories_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


