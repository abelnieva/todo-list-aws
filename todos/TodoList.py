
import boto3
from botocore.exceptions import ClientError
import decimalencoder
import json
import os
import time
import uuid


class TodoList():
    def __init__(self,table, dynamodb=None):
        self.tableName = table
        if not dynamodb:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://db:8000')
        self.dynamodb = dynamodb
    def put_item(self, data):

        
        timestamp = str(time.time())
    
        table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
        item = {
            'id': str(uuid.uuid1()),
            'text': data['text'],
            'checked': False,
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }
    
        # write the todo to the database
        table.put_item(Item=item)
        return item

        
    def list(self):
        table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
        # fetch all todos from the database
        result = table.scan()
    
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
        }
    
        return response
        
    def get_item(self, data):
        table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
        # fetch todo from the database
        result = table.get_item(
            Key={
                'id': data
            }
        )
    
        # create a response
        response = result['Item']
    
        return response
        
    def delete_item(self, data):
        table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
        # delete the todo from the database
        table.delete_item(
            Key={
                'id': data
            }
        )
    
        # create a response
        response = {
            "statusCode": 200
        }
    
        return response

  
    def update_item(self, id,data):

        timestamp = int(time.time() * 1000)
    
        table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
        # update the todo in the database
        result = table.update_item(
            Key={
                'id': id
            },
            ExpressionAttributeNames={
              '#todo_text': 'text',
            },
            ExpressionAttributeValues={
              ':text': data['text'],
              ':checked': data['checked'],
              ':updatedAt': timestamp,
            },
            UpdateExpression='SET #todo_text = :text, '
                             'checked = :checked, '
                             'updatedAt = :updatedAt',
            ReturnValues='ALL_NEW',
        )
    
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(result['Attributes'],
                               cls=decimalencoder.DecimalEncoder)
        }
    
        return response
