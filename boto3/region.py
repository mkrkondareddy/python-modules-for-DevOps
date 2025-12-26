import boto3
import json

client = boto3.client("ec2")
response = client.describe_regions()
# response= json.dumps(response, indent=2)
response= response.get("Regions")
# print(json.dumps(response, indent=2))
# print(response[0])


for i in response:
    print(f"the name of the region is: {i.get('RegionName')}")