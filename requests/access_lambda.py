import requests
from pprint import pprint

url = "https://gkz3zw7ra2wx2nzgyj7dxuh53i0bzbkj.lambda-url.us-east-1.on.aws"
headers = {
    "Content-Type": "application/json"
}

# payload = {"message": "Hello from requests"}

response = requests.get(url, headers=headers, auth=())

print(response)
pprint(response.json())