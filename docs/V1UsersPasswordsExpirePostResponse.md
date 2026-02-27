# V1UsersPasswordsExpirePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_count** | **int** |  | [optional] 
**failed_users** | [**List[IamFailedUser]**](IamFailedUser.md) |  | [optional] 
**success_count** | **int** |  | [optional] 

## Example

```python
from graphiant_sdk.models.v1_users_passwords_expire_post_response import V1UsersPasswordsExpirePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1UsersPasswordsExpirePostResponse from a JSON string
v1_users_passwords_expire_post_response_instance = V1UsersPasswordsExpirePostResponse.from_json(json)
# print the JSON string representation of the object
print(V1UsersPasswordsExpirePostResponse.to_json())

# convert the object into a dict
v1_users_passwords_expire_post_response_dict = v1_users_passwords_expire_post_response_instance.to_dict()
# create an instance of V1UsersPasswordsExpirePostResponse from a dict
v1_users_passwords_expire_post_response_from_dict = V1UsersPasswordsExpirePostResponse.from_dict(v1_users_passwords_expire_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


