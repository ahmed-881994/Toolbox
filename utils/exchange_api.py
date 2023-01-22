from . import constants
import requests

def convert(from_curr, to_curr, amount):
    url = constants.CURRENCY_CONVERT_URL+'from='+from_curr+'&to='+to_curr+'&amount='+str(amount)+'&places=2'
    response = requests.get(url)
    data = response.json()
    return data

def convert_with_date(from_curr, to_curr, amount, date):
    url = constants.CURRENCY_BASE_URL+'/'+str(date)+'?symbols='+to_curr+'&base='+from_curr+'&amount='+str(amount)+'&places=2'
    response = requests.get(url)
    data = response.json()
    return data

def get_timeseries_data(start_date, end_date, from_curr, to_curr):
    
    url = constants.CURRENCY_TIMESERIES_URL+'start_date='+start_date+'&end_date='+end_date+'&base='+from_curr+'&symbols='+to_curr+'&places=2'
    response = requests.get(url)
    data = response.json()
    return data