# AssuranceClientSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**client_endpoint** | [**AssuranceClientSessionEndpointDetails**](AssuranceClientSessionEndpointDetails.md) |  | [optional] 
**client_flex_algo** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**client_links** | [**List[AssuranceClientSessionEndpointLink]**](AssuranceClientSessionEndpointLink.md) |  | [optional] 
**client_username** | **str** |  | [optional] 
**exchange_service_name** | **str** |  | [optional] 
**first_seen_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**lan_segment** | **List[str]** |  | [optional] 
**last_seen_ts** | [**GoogleProtobufTimestamp**](GoogleProtobufTimestamp.md) |  | [optional] 
**local_dia_links** | [**List[AssuranceClientSessionDiaLink]**](AssuranceClientSessionDiaLink.md) |  | [optional] 
**pop_links** | [**List[AssuranceClientSessionPopLink]**](AssuranceClientSessionPopLink.md) |  | [optional] 
**remote_dia_links** | [**List[AssuranceClientSessionDiaLink]**](AssuranceClientSessionDiaLink.md) |  | [optional] 
**risk_status** | **str** |  | [optional] 
**server_endpoint** | [**AssuranceClientSessionEndpointDetails**](AssuranceClientSessionEndpointDetails.md) |  | [optional] 
**server_flex_algos** | **List[str]** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_links** | [**List[AssuranceClientSessionEndpointLink]**](AssuranceClientSessionEndpointLink.md) |  | [optional] 
**server_port** | **int** |  | [optional] 
**session_id** | **str** |  | [optional] 
**sla** | **str** |  | [optional] 
**sla_class** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_client_session import AssuranceClientSession

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceClientSession from a JSON string
assurance_client_session_instance = AssuranceClientSession.from_json(json)
# print the JSON string representation of the object
print(AssuranceClientSession.to_json())

# convert the object into a dict
assurance_client_session_dict = assurance_client_session_instance.to_dict()
# create an instance of AssuranceClientSession from a dict
assurance_client_session_from_dict = AssuranceClientSession.from_dict(assurance_client_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


