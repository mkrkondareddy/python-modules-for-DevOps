import requests
from pprint import pprint

data = {
    "username": "admin",
    "password": "secret"
}

response = requests.post(
    "https://httpbin.org/post",
    data=data
)

pprint(response.json())
