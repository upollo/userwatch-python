# import the package
import userwatch
# import the module from the package
from userwatch import userwatch
from userwatch import userwatch_public_pb2

testPrivateApiKey = "test"


def test_userwatch_dev():
    uw = userwatch.Userwatch(
        testPrivateApiKey, {"url": "dev.userwat.ch:443"})
    assert uw != None


def test_userwatch_local():
    uw = userwatch.Userwatch(
        testPrivateApiKey, {"url": "localhost:8080", "insecure": True})
    assert uw != None


# The following tests can be uncommented and used ad-hoc to test against a real server.

# def test_get_devices_local():
#     uw = userwatch.Userwatch(
#         testPrivateApiKey, {"url": "localhost:8080", "insecure": True})

#     resp = uw.getDeviceList(
#         "146cdba36a73703c6e54268b5df19f1531e295fe0127df638085870dba061132")
#     print("resp "+str(resp))
#     if resp.devices:
#         for device in resp.devices:
#             print("device "+str(type(device)))
#             print("device "+str(device))

#     assert False


# def test_get_devices_dev():
#     uw = userwatch.Userwatch(
#         testPrivateApiKey, {"url": "api.dev.user.watch:443"})

#     resp = uw.getDeviceList(
#         "146cdba36a73703c6e54268b5df19f1531e295fe0127df638085870dba061132")
#     print("resp "+str(resp))
#     if resp.devices:
#         for device in resp.devices:
#             print("device "+str(type(device)))
#             print("device "+str(device))

#     assert False

# def test_validate_dev():
#     uw = userwatch.Userwatch(
#         testPrivateApiKey, {"url": "api.dev.user.watch:443"})

#     resp = uw.validate(
#         "Cp0CCAIyHAgBEgsIpsv6kgYQwIz7IhoLCKbL-pIGEKiU-yIyHggYEgwI26SWkAYQ26_XugIaDAigy_qSBhDIv6SOAjoaCgtmb29AYmFyLmNvbRILZm9vQGJhci5jb21CkwEKFnp0NmNHV1dnM3RDNFRiUVREelpLaGIqeU1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDAuMC40ODk2Ljg4IFNhZmFyaS81MzcuMzZSJDJkNzdjYzA1LTNlOGQtNDFjZi1iZDZiLWYzMTNhNmJjZDkwMVoBAmABEkAFWWWTwC-tl4Ip1wtSqVAsJyG1TlEbAGlTe3qMVC7OXaGR-DFX9hSJVHXN7bo3Z6CC3GJE7LIOVYPJVEMf4IkjGgRy_Z5IIgsIq8v6kgYQyODmJA==",
#         userwatch_public_pb2.UserInfo(user_email="foo@bar.com"),
#         userwatch_public_pb2.EVENT_TYPE_LOGIN
#     )

#     if resp.action == userwatch_public_pb2.OUTCOME_PERMIT:
#         print("Outcome permit. Safe to continue.")
#     if resp.action == userwatch_public_pb2.OUTCOME_CHALLENGE:
#         print("Outcome challenge. Challenge the user with a sms code or webauthn.")
#     if resp.action == userwatch_public_pb2.OUTCOME_DENY:
#         print("Outcame deny. Deny the user.")

#     flagTypes = list(map(lambda f: f.type, resp.flags))
#     isAccountSharing = userwatch_public_pb2.FLAG_TYPE_ACCOUNT_SHARING in flagTypes
#     isRepeatedTrial = userwatch_public_pb2.FLAG_TYPE_REPEATED_SIGNUP in flagTypes

#     print("is sharing: "+str(isAccountSharing))
#     print("is repeated trial: "+str(isRepeatedTrial))

#     assert False


# def test_create_challenge_dev():
#     uw = userwatch.Userwatch(
#         testPrivateApiKey, {"url": "api.dev.user.watch:443"})

#     resp = uw.createChallenge(
#         userwatch_public_pb2.ChallengeType.CHALLENGE_TYPE_SMS,
#         userwatch_public_pb2.UserInfo(user_phone = "+61481216742"),
#         "dev_123"
#     )

#     print("create challeng: " +str(resp))

#     assert False

# def test_verify_challenge_dev():
#     uw = userwatch.Userwatch(
#         testPrivateApiKey, {"url": "api.dev.user.watch:443"})

#     resp = uw.verifyChallenge(
#         userwatch_public_pb2.ChallengeType.CHALLENGE_TYPE_SMS,
#         userwatch_public_pb2.UserInfo(user_phone = "+61481216742"),
#         "dev_123",
#         "dXQZ4pfPUKs9JBHZHyym35",
#         "35570"
#     )

#     print("verify challeng: " +str(resp))

#     assert False
