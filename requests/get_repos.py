import requests 
from pprint import pprint
import json
import os

token = os.getenv("github_token")

headers = {
    "Accept": "application/vnd.github+json"
}

response = requests.get("https://api.github.com/users/mkrkondareddy/repos", headers=headers, timeout=5, verify=True)

# pprint(response.json())
response = response.json()

print(type(response))

for i in response:
    pprint(i.get("full_name", "")) # get repo name
    print("#"*20)
