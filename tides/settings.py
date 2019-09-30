from celery.schedules import crontab

TIDES_APIKEY = 'v4qchJD73PDUsTSu60hULdMJY7aMVdjd'
BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'
CELERY_RESULT_BACKEND = 'db+sqlite:////var/lib/celery/results.db'
CELERYBEAT_SCHEDULE = {
    'auckland_tide': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*'),
        'kwargs': {
            'apikey': TIDES_APIKEY,
            'endpoint': 'https://tide.metoceanapi.com/v0/stations/{site}/timeseries',
            'site': 'auckland'
            'params': {
                'datum': 'LAT',
                'times': "{times}"
            },            
        }
    },
}
CELERYBEAT_SCHEDULE_FILENAME = '/var/lib/celery/celerybeat-schedule'
INSTALLED_APPS = ['tides.tasks']