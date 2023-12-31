import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import os

def lambda_handler(event, context):
    endpoint = f"http://{os.environ.get('LOCALSTACK_HOSTNAME')}:{os.environ.get('EDGE_PORT')}"
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url=endpoint)

    table = dynamodb.Table('LatestData')
    #name = str(event['queryStringParameters']['name'])
    #try:
    """
    response = table.query(Limit=1,
        ScanIndexForward=False,
        KeyConditionExpression="#name = :name",
        ExpressionAttributeValues={":name" : name},
        ExpressionAttributeNames= {"#name" : "name" }
    )
    """
    """
    except ClientError as err:
        return { 
            'statusCode' : 500,
            'body': {
                'sensors' : err 
                },
            'headers': {
                'Access-Control-Allow-Origin': '*'
            }
        }
    """
    response = table.scan()
    
    data = response["Items"]
    return { 
        'statusCode' : 200,
        'body': {
            'sensors' : data
            },
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'isBase64Encoded': 'false'
    }