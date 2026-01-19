# This sample script cleanups unused ebs volumes which is older then 30 minutes and not attached to any resources.

import boto3
from pprint import pprint
from datetime import datetime, timezone

current_time = datetime.now(timezone.utc)

# opens a session with AWS account to make multiple API calls in sigle session insted of seperate TCP connection for each request
session = boto3.Session()

# instanciating client # think like accessing ec2 in console 
client = session.client("ec2")

# getting ebs volumes 
response = client.describe_volumes()

response = response["Volumes"]
# pprint(response)

for volume in response:
    volume_id = volume.get("VolumeId", "")
    attachments = volume.get("Attachments", [])
    created_time = volume.get("CreateTime", "")
    age_of_volume = current_time - created_time
    print(age_of_volume)

    
    if age_of_volume.total_seconds() > 1800 and not attachments:
        print(f"volume is older than 30 minutes and volume:{volume_id} is not atatched")
        print(f"deleting volume: {volume_id}")
        
        client.delete_volume(
            VolumeId= volume_id
)
    # if not attachments:
    #     print(f"volume:{volume_id} is not atatched")