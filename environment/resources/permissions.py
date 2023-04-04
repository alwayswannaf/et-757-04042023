import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c72669a1464081l3877795t1w549186031903-s3bucket-xob545cwurbv"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")