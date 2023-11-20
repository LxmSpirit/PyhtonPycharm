import requests
from requests_mauth import MAuth

# MAuth configuration
APPUUID = "wangjunyi1"
privatekey = "@Wjy98061519"
mauth = MAuth(APPUUID, privatekey)

# Set endpoint and API version
url = "https://api.mdsol.com/countries"
headers = {"Accept": "application/json", "Mcc-Version": "v2019-04-12"}

# Make the requests call, passing the auth client and headers
result = requests.get(url, auth=mauth, headers=headers)

# Print results
print(result.status_code)
print(result.text)