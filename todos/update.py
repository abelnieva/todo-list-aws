import boto3
import json
import logging
import os
from TodoList import TodoList 

TABLE = os.environ['DYNAMODB_TABLE']
DYNAMO = boto3.resource('dynamodb')
def update(event, context):
    item = TodoList(TABLE,DYNAMO)
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        
    response = {
            "statusCode": 200,
            "body": json.dumps(item.update_item(event['pathParameters']['id'],data))
        }
    
    return response
