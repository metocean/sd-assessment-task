import requests
from celery import Celery

app = Celery('tides')

@app.task
def request_from_api(endpoint, params, apikey):
	headers = {
		'apikey' : apikey
	}
	response = requests.get(endpoint,headers=headers,params=params)
	response.raise_for_status()
	return response.json()
