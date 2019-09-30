import requests
import datetime
from celery import Celery

app = Celery('tides')

@app.task
def request_from_api(apikey, endpoint, site, params):
    headers = {
        'apikey' : apikey
    }
    endpoint = endpoint.format(site=site)
    if 'times' in params:
        time = (datetime.datetime.utcnow()).isoformat()
        params['times'] = params['times'].format(times=time)
    response = requests.get(endpoint,headers=headers,params=params)
    response.raise_for_status()
    return response.json()
