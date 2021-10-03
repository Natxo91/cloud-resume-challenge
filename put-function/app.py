import json
import boto3
from botocore.exceptions import ClientError
# import requests


def putfunction(event, context): 
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('cloud-resume-challenge')
    
    try:
        response = table.update_item(Key={"ID": "visitors"}, UpdateExpression="ADD #count :inc",
                                          ExpressionAttributeNames={'#count': 'count' },
                                          ExpressionAttributeValues={ ':inc': 1} ,
                                          ReturnValues="UPDATED_NEW")
    except ClientError as e:
        raise e
    else:
        return {
        "statusCode": 200,
            "headers": {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            }
           }
