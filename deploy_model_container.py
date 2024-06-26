'''
API to publish SCR model
'''

import time
import requests
import json
import os
from pathlib import Path
os.environ['SSLREQCERT']='false'

## server params
protocol=os.environ['PROTOCOL']
server = os.environ['SERVER']

# protocol = "https"
# server = "apgtps2demo.gtp.unx.sas.com"

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
print("Now publishing model SCR with following details:")
payload = {

    "name":"Published model scikit-learn_RandomForest",
    "notes":"Publish models",
    "modelContents": [
        {"modelName":"loanapp_model",
        "sourceUri":"/modelRepository/models/bb6ea2d6-c061-416a-a872-0de47f74c66d","publishLevel":"model"
        }],
        "destinationName":"AzureCR"
}

print(payload)

##publish module 
post_module_publish = requests.post(
    url=f'{protocol}://{server}/modelManagement/publish',
    headers={'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/vnd.sas.models.publishing.request.asynchronous+json'},
    params=dict(force='True', reloadModelTable='True'),
    data=json.dumps(payload),
    verify=False
    )

time.sleep(120)

print(post_module_publish.json())

