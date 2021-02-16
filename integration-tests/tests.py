import requests
import boto3
import botocore
import sys
import json
RECORD_ID = ""
stack = sys.argv[1]
session = boto3.Session() 
cloudformation = session.resource('cloudformation')
stack = cloudformation.Stack(stack)

public_dns = ''

for output in stack.outputs:
    if output['OutputKey'] == 'awstodolist':
        public_dns = output['OutputValue']
        break
print (public_dns)
def test_list():
    "GET request to url returns a 200"
    url = public_dns+'/todos'
    resp = requests.get(url)
    #print (resp.text)
    assert resp.status_code == 200


def test_create():
    global RECORD_ID
    "Crear un elemento"
    data = '{ "text": "Learn Serverless" }'
    r = requests.post(url = public_dns+'/todos', data = data) 
    RECORD_ID = json.loads(r.text)["id"]
    print (RECORD_ID)
    assert r.status_code == 200
    
def test_get():
    "GET request to url returns a 200"
    url = public_dns+'todos/'+RECORD_ID
    resp = requests.get(url)
    print (resp.text)
    assert resp.status_code == 200
    assert json.loads(resp.text)["text"] == "Learn Serverless"
  
test_create()
test_list()
test_get()