import requests
import boto3
import botocore
import sys
import json
RECORD_ID = ""

def test_list():
    "GET request to url returns a 200"
    url = public_dns+'/todos'
    resp = requests.get(url)
    #print (resp.text)
    assert resp.status_code == 200
    print ("OK")


def test_create():
    global RECORD_ID
    "Crear un elemento"
    data = '{ "text": "Learn Serverless" }'
    r = requests.post(url = public_dns+'/todos', data = data) 
    RECORD_ID = json.loads(r.text)["id"]
    assert r.status_code == 200
    print ("OK")
    
def test_get():
    "GET request to url returns a 200"
    url = public_dns+'todos/'+RECORD_ID
    resp = requests.get(url)
    assert resp.status_code == 200
    assert json.loads(resp.text)["text"] == "Learn Serverless"
    print ("OK")

if __name__ == "__main__":
    stack = sys.argv[1]
    session = boto3.Session() 
    cloudformation = session.resource('cloudformation')
    stack = cloudformation.Stack(stack)

    public_dns = ''

    for output in stack.outputs:
        if output['OutputKey'] == 'awstodolist':
            public_dns = output['OutputValue']
            break
    print ("Endpoint: "+public_dns)
    print ("1 - Test create Record ")
    test_create()
    print ("2 - List Records ")
    test_list()
    print ("3 - get created records ")
    test_get()