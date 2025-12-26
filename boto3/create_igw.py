import boto3
import json 

client = boto3.client("ec2")

response = client.create_internet_gateway(
    TagSpecifications = [ {
        "ResourceType": "internet-gateway",
        "Tags": [
            {
                "Key": "Name",
                "Value": "boto3-igw"
            }
        ]
    } ]
)

print(response)