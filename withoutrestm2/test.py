import requests
import json

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
# def get_resources(id=None):
#     data={}
#     if id is not None:
#         data={'id':id}
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources(5)

# def create_resources():
#     new_std={
#     'name':'psi',
#     'rollno':106,
#     'marks':42,
#     'gf':'psicho',
#     'bf':'psichopath',
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
#     print(resp.status_code)
#     print(resp.json())
# create_resources()

# def update_resources(id=None):
#     new_data={
#     'id':id,
#     'gf':'deepika'
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
# update_resources(4)

def delete_resource(id):
    data={
    'id':id,
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(4)
