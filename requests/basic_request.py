import requests
import json
from pprint import pprint
response = requests.get("https://httpbin.org/get")

# print(dir(response))

# print("#"*30)

# get text response (json text)
print(response.text)

# cehck type of response.text
print(type(response.text))

# convert json text into python dictionary
print(json.loads(response.text))

# print response code
print(response.status_code)

# print json response
print(response.json())