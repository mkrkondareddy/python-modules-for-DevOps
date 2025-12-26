import boto3
import json

client = boto3.client("ec2")
response = client.delete_internet_gateway(
    InternetGatewayId='igw-0b58c10bb8ab34468'
)

print(response)