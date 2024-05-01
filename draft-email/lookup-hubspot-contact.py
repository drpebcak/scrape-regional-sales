import os

import requests

name = os.environ["NAME"]
token = os.environ["HUBSPOT_ACCESS_TOKEN"]

url = "https://api.hubapi.com/settings/v3/users/"

querystring = {"limit": "10", "archived": "false"}

headers = {
    'accept': "application/json",
    'authorization': 'Bearer %s' % token
}

response = requests.request("GET", url, headers=headers, params=querystring)

for item in response.json()["results"]:
    if item["firstName"] == name:
        print(item["email"])
        exit(0)

exit(1)