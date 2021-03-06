'''
====================
Boto 3 - EC2 Example
====================
This application implements the EC2 service that lets you gets
information from Amazon EC2. See the README for more details.
'''
import boto3
import json

config = json.loads(open('config/defaults.json').read())
credentials = config['credentials']

AWS_ACCESS_KEY_ID = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = credentials['aws_secret_access_key']
REGION_NAME = 'us-west-1'

ec2 = boto3.client('ec2',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=REGION_NAME)

print ec2.describe_regions()
print
print ec2.describe_instances()
print