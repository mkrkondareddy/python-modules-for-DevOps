import requests
import json
import os

token = os.getenv("github_token")

url = "https://api.github.com/repos/mkrkondareddy/Agentic-workflows"

headers = {
     "Accept" : "application/vnd.github+json",
     "Authorization" : f"Bearer {token}",
     "X-GitHub-Api-Version" : "2022-11-28"
}
response = requests.delete(url=url, headers=headers)
print(type(response))
print(response.text)
print(response.status_code)
