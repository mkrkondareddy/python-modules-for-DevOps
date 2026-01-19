import boto3
from pprint import pprint


client = boto3.client("ec2")


# it only returns instances with tag "environment=dev"
response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:environment',
            'Values': [
                'dev',
            ],
        },
    ],
)

pprint(response)