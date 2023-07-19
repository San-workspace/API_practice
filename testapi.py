import sys
import requests
import json

import warnings

warnings.filterwarnings('ignore', message='Unverified HTTPS request')

url = "https://dm.rbei-energymanager.com/api/shadow"

Shadow_Payload = {
  "applId": "em",
  "tenantId": "50000001",
  "devName": "em_50000001_2",
  "applTenant": "11111111",
  "shadow": {
    "state": {
      "desired": {
        "ota": "n",
        "mode": "normal",
        "firmware": "0",
        "modelchange": "n"
      }
    }
  }
}

payload = json.dumps(Shadow_Payload)

headers = {
  'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjI1N2U1ZDgzMGMwM2M0NDUxYzc3Y2Q4IiwiZW1haWwiOiJqYW5hcmRoYW4uYWJoaWxhc2hAaW4uYm9zY2guY29tIiwidGVuYW50SWQiOiIxMTExMTExMSIsInN5c1JvbGUiOiJTeXN0ZW1Vc2VyIiwiYXBwUm9sZXMiOltdLCJ1c2VyUm9sZSI6W10sImlhdCI6MTY4ODYzMzk2MiwiZXhwIjoxNjg4NjQzOTYyfQ.jPzQQ404ULbgZNNknV_EtMGTEQtk45VyrxXRWtP6CUc'
}

proxies = {
'http' : '127.0.0.1:3128',
'https' : '127.0.0.1:3128',
'no_proxy':'localhost,127.1.1.0,127.0.0.1,.bosch.com',
}

response = requests.request("PUT", url, headers=headers, data=payload, proxies=proxies, verify=False)
print(payload)
req_response = response.json()
print(req_response)


