import boto3
import uuid
import datetime
import json

id = str(uuid.uuid4())
timestamp = int(datetime.datetime.now().timestamp())

sqs = boto3.client('sqs', aws_access_key_id=None, aws_secret_access_key=None, endpoint_url='http://localhost:4566')
queue_url = 'http://localhost:4566/000000000000/sqs_queue'

message = {
    "uuid": id,
    "name": "Sensor",
    "latitude": 10,
    "longitude": 10,
    "timestamp": timestamp,
    "windSpeed": 10,
    "windDirection": "S"
}

resp = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(
        json.dumps(message)
    )
)
print(resp['MessageId'])