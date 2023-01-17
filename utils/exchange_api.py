from . import constants
import requests
import json

def convert(from_curr, to_curr, amount):
    url = constants.CURRENCY_CONVERT_URL+'from='+from_curr+'&to='+to_curr+'&amount='+str(amount)
    response = requests.get(url)
    data = response.json()
    return data