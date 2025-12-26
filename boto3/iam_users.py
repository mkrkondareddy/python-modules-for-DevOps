import boto3
import json 
from pprint import pprint
from datetime import datetime, timezone


current_time = datetime.now(timezone.utc)

client = boto3.client('iam')
response = client.list_users()
# responce = json.dumps(response, indent=4, default=str)
response= response.get("Users", [])
# pprint(response)


for i in response:
    user= i.get("UserName", "" )
    create_date= i.get("CreateDate", "")
    print(f"User: {user}, Created on: {create_date}")
    age_of_user= current_time-create_date
    print(f"Age of User: {age_of_user.days} days")
    
    if age_of_user.days < 30:
        print(f"User {user} is younger than 30 days.")
        response = client.list_attached_user_policies(
            UserName=user,
            PathPrefix= "/"
        )
        
        # pprint(response)
        attached_policy_arn = response.get("AttachedPolicies", [])
        for policy in attached_policy_arn:
            policy_arn = policy.get("PolicyArn", "")
            print(f"Detaching policy {policy_arn} from user {user}")

            response = client.detach_user_policy(
                UserName=user,
                PolicyArn=policy_arn
            )
        print(f"All policies detached from user {user}.")
        
        access_keys = []
        print(f"getting access keys for user: {user}")
        response = client.list_access_keys(
            UserName=user,
        )
        keys = response.get("AccessKeyMetadata", [])
        for key in keys:
            access_key_id = key.get("AccessKeyId", "")
            access_keys.append(access_key_id)
        print(access_keys)

        print(f"deleting access keys for user: {user}")
        for access_key in access_keys:
            response = client.delete_access_key(
                UserName=user,
                AccessKeyId=access_key
            )
        
        response = client.delete_user(
            UserName=user
            )
        print(f"user deleted successfully: {user}")
    # print("####################################")


