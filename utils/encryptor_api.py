from . import constants
import requests
import json

def encrypt(method:str, payload):
    method = method.lower().replace(' ','')
    url = constants.ENCRYPTOR_URL + method

    payload = json.dumps(payload)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()
