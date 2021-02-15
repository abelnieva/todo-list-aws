import os
import json
import decimalencoder
import boto3
from TodoList import TodoList 

TABLE = os.environ['DYNAMODB_TABLE']
DYNAMO = boto3.resource('dynamodb')


def translate(event, context):
    item = TodoList(TABLE,DYNAMO)
    data = event['pathParameters']['id']
    translate = boto3.client('translate')
    result=item.get_item(data)
    result_text = translate.translate_text(Text=result["text"],
                                  SourceLanguageCode="auto",
                                  TargetLanguageCode=event['pathParameters']['language'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result_text,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
