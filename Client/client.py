import json
import requests

# endpoints
base_end_point = 'http://127.0.0.1:8000/api'
token_end_point = base_end_point+'/token/'
sa_endpoint = base_end_point+'/make_sa_inference'

# credentials
username = 'ElonMusk'
password = 'ilovenasa'

# Authentication
credential = {'username':username,
               'password':password}
headers = {'Content-Type':'application/json'}
r1 = requests.post(token_end_point,data=json.dumps(credential),headers=headers)
token = r1.json()['token']
headers['Authorization'] = 'Bearer '+token

# Analyse some text
text_to_analyze = 'i love Blogging'
json_data = json.dumps({'text':text_to_analyze})
r2 = requests.post(sa_endpoint,data=json_data,headers=headers)
result = r2.json()['result']
print(result)
