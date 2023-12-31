import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")

table = dynamodb.create_table(
    TableName = 'WindData',
    KeySchema = [
        {
            'AttributeName': 'sensorName',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'createdAt',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'sensorName',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'createdAt',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)

table = dynamodb.create_table(
    TableName = 'LatestData',
    KeySchema = [
        {
            'AttributeName': 'sensorName',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'createdAt',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'sensorName',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'createdAt',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)
