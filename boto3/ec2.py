import boto3
import json 
from pprint import pprint

client = boto3.client("ec2")
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'test-vm',
            ],
        },
    ],
)

# pprint(response)
# response = json.dumps(response, indent=2, default=str)
# pprint(response)
response = response["Reservations"]

for i in response:
    instance_id = i.get("Instances", [])[0].get("InstanceId", "")
    if instance_id == "i-0b2f9bf9a3dcbfdbd":
        response = client.terminate_instances(InstanceIds=[instance_id])
        pprint(response)