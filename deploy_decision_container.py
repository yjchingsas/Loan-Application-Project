'''
API to publish SCR model
'''

import requests
import json
import os
from pathlib import Path
os.environ['SSLREQCERT']='false'

## server params
protocol=os.environ['PROTOCOL']
server = os.environ['SERVER']

# dest_name = os.environ['DESTINATION_NAME']
# model_name = os.environ['MODEL_NAME']

## Refresh token
refresh_token = Path('demo/apgtps2demo_refresh_token.txt').read_text().replace('\n', '')

payload=f'grant_type=refresh_token&refresh_token={refresh_token}'
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic c2FzLmNsaTo=',
}

response = requests.post(
    url = f"{protocol}://{server}/SASLogon/oauth/token", 
    headers=headers, 
    data=payload,
    verify=False
)
access_token = response.json()['access_token']

## publishing time
print("Now publishing decision SCR with following details:")
payload = {
    "notes": "Published by SAS Intelligent Decisioning",
    "destinationName": "AzureCR",
    "modelContents": [
        {
            "overwrite": True,
            "modelName": "loanapp_project",
            "codeMediaType": "text/vnd.sas.source.ds2.async",
            "codeType": "ds2",
            "codeUri": "/decisions/flows/69825e91-8b52-4f7e-9bff-b46f1a89e0ba/revisions/3de0a4dc-80ea-4e16-9114-3bf8a5adae13/code?rootPackageName=loanapp_project&traversedPathFlag=false&isGeneratingRuleFiredColumn=false&codeTarget=docker",
            "publishLevel": "decision",
            "sourceUri": "/decisions/flows/69825e91-8b52-4f7e-9bff-b46f1a89e0ba/revisions/3de0a4dc-80ea-4e16-9114-3bf8a5adae13",
            "principalID": "69825e91-8b52-4f7e-9bff-b46f1a89e0ba",
            "analyticStoreUri": []
        }]
}



print(payload)

##publish module 
post_module_publish = requests.post(
    url=f'{protocol}://{server}/modelPublish/models',
    headers={'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/vnd.sas.models.publishing.request+json'},
    params=dict(force='True'),
    data=json.dumps(payload),
    verify=False
    )
print(post_module_publish.json())