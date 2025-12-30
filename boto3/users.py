import boto3
import json
from pprint import pprint 

client = boto3.client("iam")

response = client.list_users()
response = response.get("Users", [])

pprint(response)

# print(type(response))
# for user in response:
#     print(user.get("UserName", ""))