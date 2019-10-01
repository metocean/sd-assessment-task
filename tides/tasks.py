import requests
import datetime
import time
from celery import Celery

app = Celery('tides')

@app.task
def request_from_api(apikey, endpoint, params):
    headers = {
        'apikey' : apikey
    }
    response = requests.get(endpoint,headers=headers,params=params)
    response.raise_for_status()
    return response.json()