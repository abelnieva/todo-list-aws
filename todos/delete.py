import boto3
import json
import os
from TodoList import TodoList 

TABLE = os.environ['DYNAMODB_TABLE']
DYNAMO = boto3.resource('dynamodb')
def delete(event, context):
    item = TodoList(TABLE,DYNAMO)
    data = event['pathParameters']['id']
        
    response = {
            "statusCode": 200,
            "body": json.dumps(item.delete_item(data))
        }
    
    return response
