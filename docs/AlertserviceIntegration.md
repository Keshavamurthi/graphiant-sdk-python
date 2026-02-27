# AlertserviceIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**details** | [**AlertserviceIntegrationDetails**](AlertserviceIntegrationDetails.md) |  | [optional] 
**enterprise_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**last_scanned** | **int** | last scanned time for integrations (zendesk) | [optional] 
**nick_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.alertservice_integration import AlertserviceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AlertserviceIntegration from a JSON string
alertservice_integration_instance = AlertserviceIntegration.from_json(json)
# print the JSON string representation of the object
print(AlertserviceIntegration.to_json())

# convert the object into a dict
alertservice_integration_dict = alertservice_integration_instance.to_dict()
# create an instance of AlertserviceIntegration from a dict
alertservice_integration_from_dict = AlertserviceIntegration.from_dict(alertservice_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


