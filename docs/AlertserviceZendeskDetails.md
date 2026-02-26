# AlertserviceZendeskDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zendesk_api_token** | **str** | zendesk api token (required) | 
**zendesk_assignee_id** | **str** | zendesk assignee id (required) | 
**zendesk_base_url** | **str** | zendesk base url (required) | 
**zendesk_email** | **str** | zendesk email (required) | 

## Example

```python
from graphiant_sdk.models.alertservice_zendesk_details import AlertserviceZendeskDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AlertserviceZendeskDetails from a JSON string
alertservice_zendesk_details_instance = AlertserviceZendeskDetails.from_json(json)
# print the JSON string representation of the object
print(AlertserviceZendeskDetails.to_json())

# convert the object into a dict
alertservice_zendesk_details_dict = alertservice_zendesk_details_instance.to_dict()
# create an instance of AlertserviceZendeskDetails from a dict
alertservice_zendesk_details_from_dict = AlertserviceZendeskDetails.from_dict(alertservice_zendesk_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


