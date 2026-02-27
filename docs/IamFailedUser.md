# IamFailedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from graphiant_sdk.models.iam_failed_user import IamFailedUser

# TODO update the JSON string below
json = "{}"
# create an instance of IamFailedUser from a JSON string
iam_failed_user_instance = IamFailedUser.from_json(json)
# print the JSON string representation of the object
print(IamFailedUser.to_json())

# convert the object into a dict
iam_failed_user_dict = iam_failed_user_instance.to_dict()
# create an instance of IamFailedUser from a dict
iam_failed_user_from_dict = IamFailedUser.from_dict(iam_failed_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


