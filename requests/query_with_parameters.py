import requests
from pprint import pprint

params = {
    "page": 1,
    "limit": 10
}

response = requests.get(
    "https://httpbin.org/get",
    params=params
)

pprint(response.json())
