# V1UsersPasswordsExpirePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 

## Example

```python
from graphiant_sdk.models.v1_users_passwords_expire_post_request import V1UsersPasswordsExpirePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersPasswordsExpirePostRequest from a JSON string
v1_users_passwords_expire_post_request_instance = V1UsersPasswordsExpirePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UsersPasswordsExpirePostRequest.to_json())

# convert the object into a dict
v1_users_passwords_expire_post_request_dict = v1_users_passwords_expire_post_request_instance.to_dict()
# create an instance of V1UsersPasswordsExpirePostRequest from a dict
v1_users_passwords_expire_post_request_from_dict = V1UsersPasswordsExpirePostRequest.from_dict(v1_users_passwords_expire_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


