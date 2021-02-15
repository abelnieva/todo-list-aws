import boto3
from botocore.exceptions import ClientError
import time
import uuid


class todoTable(object):

    def __init__(self, table, dynamodb=None):
        self.tableName = table
        if not dynamodb:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://db:8000')
        self.dynamodb = dynamodb

    def create_todo_table(self):
        table = self.dynamodb.create_table(
            TableName=self.tableName,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter(
            'table_exists').wait(TableName=self.tableName)
        if (table.table_status != 'ACTIVE'):
            raise AssertionError()

        return table

    def delete_todo_table(self):
        table = self.dynamodb.Table(self.tableName)
        table.delete()

    def put_todo(self, text, id=None):
        table = self.dynamodb.Table(self.TableName)
        timestamp = str(time.time())

        try:
            response = table.put_item(
                Item={
                    'id': id,
                    'text': text,
                    'checked': False,
                    'createdAt': timestamp,
                    'updatedAt': timestamp,
                })
    
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def get_todo(self, id):
        table = self.dynamodb.Table(self.tableName)
    
        try:
            response = table.get_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response


    def scan_todo(self,id):
        table = self.dynamodb.Table(self.tableName)
    
        try:
            # fetch all todos from the database
            response = table.scan()
    
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response


    def update_todo(self, text, id, checked, dynamodb=None):
        table = self.dynamodb.Table(self.tableName)
        timestamp = str(time.time())
    
        try:
            response = table.update_item(
                Key={
                    'id': id
                },
                ExpressionAttributeNames={
                    '#todo_text': 'text',
                },
                ExpressionAttributeValues={
                    ':text': text,
                    ':checked': checked,
                    ':updatedAt': timestamp,
                },
                UpdateExpression='SET #todo_text = :text, '
                                 'checked = :checked, '
                                 'updatedAt = :updatedAt',
                ReturnValues='ALL_NEW',
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response

    def delete_todo(self, id):
        table = self.dynamodb.Table(self.tableName)
    
        try:
            # delete the todo from the database
            response = table.delete_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response