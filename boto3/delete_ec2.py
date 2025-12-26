import boto3
import json


def delete_ec2_instance(instance_id):
    client = boto3.client("ec2")
    response = client.terminate_instances(
        InstanceIds=[instance_id],
    )
    
delete_ec2_instance("i-0b2f9bf9a3dcbfdbd")