# AlertserviceIntegrationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opsgenie_key** | **str** |  | [optional] 
**opsramp_details** | **str** |  | [optional] 
**pagerduty_routing_key** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**zendesk_details** | [**AlertserviceZendeskDetails**](AlertserviceZendeskDetails.md) |  | [optional] 

## Example

```python
from graphiant_sdk.models.alertservice_integration_details import AlertserviceIntegrationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AlertserviceIntegrationDetails from a JSON string
alertservice_integration_details_instance = AlertserviceIntegrationDetails.from_json(json)
# print the JSON string representation of the object
print(AlertserviceIntegrationDetails.to_json())

# convert the object into a dict
alertservice_integration_details_dict = alertservice_integration_details_instance.to_dict()
# create an instance of AlertserviceIntegrationDetails from a dict
alertservice_integration_details_from_dict = AlertserviceIntegrationDetails.from_dict(alertservice_integration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


