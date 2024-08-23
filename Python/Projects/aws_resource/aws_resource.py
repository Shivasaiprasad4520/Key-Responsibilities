#!/usr/bin/env python3

###############################################################################
# Author: Shivasai
# Version: v0.0.1
#
# Script to automate the process of listing all the resources in an AWS account
#
# Below are the services that are supported by this script:
# 1. EC2
# 2. RDS
# 3. S3
# 4. CloudFront
# 5. VPC
# 6. IAM
# 7. Route53
# 8. CloudWatch
# 9. CloudFormation
# 10. Lambda
# 11. SNS
# 12. SQS
# 13. DynamoDB
# 14. VPC
# 15. EBS
#
# The script will prompt the user to enter the AWS region and the service for 
# which the resources need to be listed.
#
# Usage: ./aws_resource_list.py <aws_region> <aws_service>
# Example: ./aws_resource_list.py us-west-1 ec2
###############################################################################

import sys
import boto3
import botocore

# Check if the required number of arguments are passed
if len(sys.argv) != 3:
    print("Usage: ./aws_resource_list.py <aws_region> <aws_service>")
    print("Example: ./aws_resource_list.py us-east-1 ec2")
    sys.exit(1)

# Assign the arguments to variables
aws_region = sys.argv[1]
aws_service = sys.argv[2].lower()

# Check if the AWS CLI is configured (boto3 uses the same config)
try:
    boto3.setup_default_session(region_name=aws_region)
except botocore.exceptions.NoCredentialsError:
    print("AWS CLI is not configured. Please configure the AWS CLI and try again.")
    sys.exit(1)

# Function to list resources based on the service
def list_resources(service):
    if service == 'ec2':
        print(f"Listing EC2 Instances in {aws_region}")
        ec2 = boto3.client('ec2', region_name=aws_region)
        response = ec2.describe_instances()
    elif service == 'rds':
        print(f"Listing RDS Instances in {aws_region}")
        rds = boto3.client('rds', region_name=aws_region)
        response = rds.describe_db_instances()
    elif service == 's3':
        print("Listing S3 Buckets")
        s3 = boto3.client('s3')
        response = s3.list_buckets()
    elif service == 'cloudfront':
        print(f"Listing CloudFront Distributions in {aws_region}")
        cloudfront = boto3.client('cloudfront', region_name=aws_region)
        response = cloudfront.list_distributions()
    elif service == 'vpc':
        print(f"Listing VPCs in {aws_region}")
        ec2 = boto3.client('ec2', region_name=aws_region)
        response = ec2.describe_vpcs()
    elif service == 'iam':
        print("Listing IAM Users")
        iam = boto3.client('iam')
        response = iam.list_users()
    elif service == 'route53':
        print("Listing Route53 Hosted Zones")
        route53 = boto3.client('route53')
        response = route53.list_hosted_zones()
    elif service == 'cloudwatch':
        print(f"Listing CloudWatch Alarms in {aws_region}")
        cloudwatch = boto3.client('cloudwatch', region_name=aws_region)
        response = cloudwatch.describe_alarms()
    elif service == 'cloudformation':
        print(f"Listing CloudFormation Stacks in {aws_region}")
        cloudformation = boto3.client('cloudformation', region_name=aws_region)
        response = cloudformation.describe_stacks()
    elif service == 'lambda':
        print(f"Listing Lambda Functions in {aws_region}")
        lambda_client = boto3.client('lambda', region_name=aws_region)
        response = lambda_client.list_functions()
    elif service == 'sns':
        print(f"Listing SNS Topics in {aws_region}")
        sns = boto3.client('sns', region_name=aws_region)
        response = sns.list_topics()
    elif service == 'sqs':
        print(f"Listing SQS Queues in {aws_region}")
        sqs = boto3.client('sqs', region_name=aws_region)
        response = sqs.list_queues()
    elif service == 'dynamodb':
        print(f"Listing DynamoDB Tables in {aws_region}")
        dynamodb = boto3.client('dynamodb', region_name=aws_region)
