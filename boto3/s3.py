import boto3
import json
from pprint import pprint

client = boto3.client('s3')
response = client.list_buckets()

response = response.get('Buckets', [])
# pprint(response)

for bucket in response:
    print(bucket.get("Name", ""))