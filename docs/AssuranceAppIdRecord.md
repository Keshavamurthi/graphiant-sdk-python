# AssuranceAppIdRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_hosts** | **int** |  | [optional] 
**affected_regions** | **int** |  | [optional] 
**affected_sites** | **int** |  | [optional] 
**affected_vrfs** | **int** |  | [optional] 
**app_id_key** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**app_type** | **str** |  | [optional] 
**blocked_policy_list** | **List[str]** |  | [optional] 
**blocked_reason_list** | **List[str]** |  | [optional] 
**category** | **str** |  | [optional] 
**classfication_field** | **str** |  | [optional] 
**classification_field** | **str** |  | [optional] 
**clients** | **List[str]** |  | [optional] 
**exchange_service** | [**List[AssuranceExchangeServiceIdentifier]**](AssuranceExchangeServiceIdentifier.md) |  | [optional] 
**first_seen** | **int** |  | [optional] 
**flex_algo** | [**List[AssuranceFlexAlgoIdentifier]**](AssuranceFlexAlgoIdentifier.md) |  | [optional] 
**flows_analyzed** | **int** |  | [optional] 
**last_seen** | **int** |  | [optional] 
**new_ip_hint** | **bool** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**region_list** | **List[str]** |  | [optional] 
**risk_status** | **str** |  | [optional] 
**server_ip** | **str** |  | [optional] 
**server_port** | **str** |  | [optional] 
**site_list** | **List[str]** |  | [optional] 
**threat_score** | **int** |  | [optional] 
**vrf_list** | **List[str]** |  | [optional] 

## Example

```python
from graphiant_sdk.models.assurance_app_id_record import AssuranceAppIdRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AssuranceAppIdRecord from a JSON string
assurance_app_id_record_instance = AssuranceAppIdRecord.from_json(json)
# print the JSON string representation of the object
print(AssuranceAppIdRecord.to_json())

# convert the object into a dict
assurance_app_id_record_dict = assurance_app_id_record_instance.to_dict()
# create an instance of AssuranceAppIdRecord from a dict
assurance_app_id_record_from_dict = AssuranceAppIdRecord.from_dict(assurance_app_id_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


