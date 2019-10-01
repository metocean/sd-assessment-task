from celery.schedules import crontab
import datetime

TIDES_APIKEY = 'v4qchJD73PDUsTSu60hULdMJY7aMVdjd'
BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'
CELERY_RESULT_BACKEND = 'db+sqlite:////var/lib/celery/results.db'


CELERYBEAT_SCHEDULE = {
    'auckland_timeserie': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*/5'),
        'kwargs': {
            'apikey': TIDES_APIKEY,
            'endpoint': 'https://tide.metoceanapi.com/v0/stations/auckland/timeseries',
            'params': {
                'datum': 'LAT',
            },            
        }
    },
    'onehunga_tidetimes': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*'),
        'kwargs': {
            'apikey': TIDES_APIKEY,
            'endpoint': 'https://tide.metoceanapi.com/v0/stations/onehunga/tidetimes',
            'params': {
                'datum': 'LAT',
                'times': datetime.datetime.utcnow().isoformat()
            },            
        }
    },
    'dunedin_timeseries': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*/5'),
        'kwargs': {
            'apikey': TIDES_APIKEY,
            'endpoint': 'https://tide.metoceanapi.com/v0/stations/dunedin/timeseries',
            'params': {
                'datum': 'LAT',
                'times': "2019-01-01"
            },            
        }
    },
    'dunedin_constituents': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*'),
        'kwargs': {
            'apikey': TIDES_APIKEY,
            'endpoint': 'https://tide.metoceanapi.com/v0/stations/dunedin/constituents',
            'params': {
                'datum': 'LAT',
            },            
        }
    },
    'all_stations': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*/10'),
        'kwargs': {
            'apikey': TIDES_APIKEY,
            'endpoint': 'https://tide.metoceanapi.com/v0/stations/',
            'params': {
                'datum': 'LAT',
            },            
        }
    },
}
CELERYBEAT_SCHEDULE_FILENAME = '/var/lib/celery/celerybeat-schedule'
INSTALLED_APPS = ['tides.tasks']