import boto3
from pprint import pprint
from datetime import datetime, UTC

client = boto3.client('s3')

response = client.list_buckets()

# pprint(response.get("Buckets", []))
buckets = response.get("Buckets", [])

current_time = datetime.now(UTC)
print(current_time)

# old_time = "2023-03-22 17:00:45+00:00"
# age = current_time-old_time
# print(age)

for bucket in buckets:
    name = bucket["Name"]
    created = bucket.get("CreationDate", "")
    # print(f"the name of the bucket is: {name}")
    # print(f"created on: {created}")
    
    age_of_bucket = current_time - created
    # print(dir(age_of_bucket))
    # print(age_of_bucket)
    
    if age_of_bucket.days > 1200:
        print(name)