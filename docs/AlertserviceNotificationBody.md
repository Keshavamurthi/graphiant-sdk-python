# AlertserviceNotificationBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of notification | [optional] 
**duration** | **str** | Time interval for notification (required) | [optional] 
**enabled** | **bool** | Enable or disable notification (required) | [optional] 
**frequency** | **int** | Frequency of notifying a continuing alert (required) | [optional] 
**message_body** | **str** | Message body to prepend to actual message | [optional] 
**notification_name** | **str** | Name of the notification record (required) | [optional] 
**opsgenie_list** | **List[str]** |  | [optional] 
**opsramp_list** | **List[str]** |  | [optional] 
**pagerduty_list** | **List[str]** |  | [optional] 
**recipient_list** | **List[str]** |  | [optional] 
**teams_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.alertservice_notification_body import AlertserviceNotificationBody

# TODO update the JSON string below
json = "{}"
# create an instance of AlertserviceNotificationBody from a JSON string
alertservice_notification_body_instance = AlertserviceNotificationBody.from_json(json)
# print the JSON string representation of the object
print(AlertserviceNotificationBody.to_json())

# convert the object into a dict
alertservice_notification_body_dict = alertservice_notification_body_instance.to_dict()
# create an instance of AlertserviceNotificationBody from a dict
alertservice_notification_body_from_dict = AlertserviceNotificationBody.from_dict(alertservice_notification_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


