import requests
import json

token = "ghp_0foq4simjLneithP"

url = "https://api.github.com/repos/mkrkondareddy/Hello-World"

headers = {
     "Accept" : "application/vnd.github+json",
     "Authorization" : f"Bearer {token}",
     "X-GitHub-Api-Version" : "2022-11-28"
}
response = requests.delete(url=url, headers=headers)
print(type(response))
print(response.text)
print(response.status_code)
