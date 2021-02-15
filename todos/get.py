import boto3
import json
import logging
import os
from TodoList import TodoList 
import decimalencoder

TABLE = os.environ['DYNAMODB_TABLE']
DYNAMO = boto3.resource('dynamodb')
def get(event, context):
    item = TodoList(TABLE,DYNAMO)
    data = event['pathParameters']['id']
    response = {
        "statusCode": 200,
        "body": json.dumps(item.get_item(data),
                           cls=decimalencoder.DecimalEncoder)
    }
    return response
