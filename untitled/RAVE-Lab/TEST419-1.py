import requests
from requests_mauth import MAuth

# MAuth configuration
#APP_UUID = "<MAUTH_APP_UUID>"
#private_key = open("private.key", "r").read()
APP_UUID = "wangjunyi1"
private_key = "@Wjy98061519"
mauth = MAuth(APP_UUID, private_key)

# Call an MAuth protected resource, in this case an iMedidata API
# listing the studies for a particular user
user_uuid = "10ac3b0e-9fe2-11df-a531-12313900d531"
url = "https://innovate.imedidata.com/api/v2/users/%s/studies.json" % user_uuid

# Make the requests call, passing the auth client
result = requests.get(url, auth=mauth)

# Print results
if result.status_code == 200:
    print([r["uuid"] for r in result.json()["studies"]])
print(result.text)