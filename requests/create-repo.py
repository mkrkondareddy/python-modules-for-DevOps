import requests
from pprint import pprint
import json
import os


url =  "https://api.github.com/user/repos"
token = os.getenv("github_token")

pay_load = {
    "name":"Hello-World",
    "description":"This is your first repository",
    "homepage":"https://github.com",
    "private":False,
    "has_issues":True,
    "has_projects":True,
    "has_wiki":True
}

headers = {
    "Accept" : "application/vnd.github+json",
    "Authorization" : f"Bearer {token}",
    "X-GitHub-Api-Version" : "2022-11-28"
}

response = requests.post(url=url, headers=headers, json=pay_load)

print(response)
print(response.json())