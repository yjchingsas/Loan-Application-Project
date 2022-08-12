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
refresh_token = Path('demo/sas_cli_refresh_token.txt').read_text().replace('\n', '')

payload=f'grant_type=refresh_token&refresh_token={refresh_token}'
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic c2FzLmNsaTo=',
}

response = requests.post(
    url = f"{protocol}://{server}/SASLogon/oauth/token", 
    headers=headers, 
    data=payload
)
access_token = response.json()['access_token']

## publishing time
payload = {
    "notes":"Published by SAS Intelligent Decisioning",
    "destinationName":"Azure",
    "modelContents":[
     {"overwrite":True,
      "modelName":"loanapp_project",
      "codeMediaType":"text/vnd.sas.source.ds2.async",
      "codeType":"ds2",
      "codeUri":"/decisions/flows/ae9973b5-8343-4288-8254-ce87981829a4/revisions/05257f25-9d71-4428-8973-44cc61ee4277/code?rootPackageName=loanapp_project_test&traversedPathFlag=false&isGeneratingRuleFiredColumn=false&codeTarget=docker",
      "publishLevel":"decision",
      "sourceUri":"/decisions/flows/ae9973b5-8343-4288-8254-ce87981829a4/revisions/05257f25-9d71-4428-8973-44cc61ee4277",
      "principalID":"ae9973b5-8343-4288-8254-ce87981829a4",
     }]
}

##publish module 
post_module_publish = requests.post(
    url=f'{protocol}://{server}/modelPublish/models',
    headers={'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/vnd.sas.models.publishing.request+json'},
    params=dict(force='True'),
    data=json.dumps(payload)
    )
post_module_publish.json()