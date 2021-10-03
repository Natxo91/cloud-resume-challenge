import json
import boto3
from botocore.exceptions import ClientError
# import requests


def getfunction(event, context):
    
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('cloud-resume-challenge')
    
    try:
        response = table.get_item(Key={'ID': 'visitors'})
    except ClientError as e:
        raise e
    else:
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({"count" : "{0}".format(str(response['Item'].get('count')))})
    }
