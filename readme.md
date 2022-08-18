# Upollo Python Client

The [Upollo](https://upollo.ai) Python library can be used identify users before they login or if they visit from multiple devices.

The Python library runs on your server and can be paired with the web or mobile to protect logins or payments.

## Get your API Keys

Sign up for our beta at [upollo.ai/beta](https://upollo.ai/beta) to get your Private API key.

## Getting started

Import the package and create a client with your api key.

```python
from userwatch import userwatch

privateApiKey = "ADD_PRIVATE_API_KEY_HERE"
userwatchClient = userwatch.Userwatch(privateApiKey)
```

## Validate a User

To validate a user you need a token from the javascript library. See the [Upollo Javascript Client Guide](https://upollo.ai/docs/web-library) for how to get the token.

You also need a userId and possibly their email address or phone number, whichever is available to improve detection. You can use an email address as the id if you don't have another id.

```python
from userwatch import userwatch
from userwatch import userwatch_public_pb2

userwatchToken = "GET FROM THE WEB CLIENT"

userInfo = userwatch_public_pb2.UserInfo(
    user_id="u_1234", # provide your user id if you have it.
    user_name="foo", # provide user name if you have it.
    user_email="foo@bar.com", # provide the email address if you have it.
    user_phone="+6100000000", # provide the phone number if you have it
)

eventType = userwatch_public_pb2.EVENT_TYPE_LOGIN

analysis = userwatchClient.verify(
  userwatchToken,
  userInfo
)

flagTypes = list(map(lambda f: f.type, analysis.flags))
isAccountSharing = userwatch_public_pb2.ACCOUNT_SHARING in flagTypes
isRepeatedTrial = userwatch_public_pb2.REPEATED_SIGNUP in flagTypes

if isAccountSharing:
    print("user is account sharing")

if isRepeatedTrial:
    print("user is repeating trial")
```
