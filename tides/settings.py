from celery.schedules import crontab

TIDES_APIKEY = 'v4qchJD73PDUsTSu60hULdMJY7aMVdjd'
BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'
CELERY_RESULT_BACKEND = 'db+sqlite:////var/lib/celery/results.db'

def schedule_gen(stations):
    schedules = {}
    for station in stations:
        schedules[station+'_tide'] = {
            'task': 'tides.tasks.request_from_api',
            'schedule': crontab(minute='*'),
            'kwargs': {
                'apikey': TIDES_APIKEY,
                'endpoint': 'https://tide.metoceanapi.com/v0/stations/{station}/timeseries',
                'station': station,
                'params': {
                    'datum': 'LAT',
                    'times': "{times}"
                },            
            }
        }
    return schedules

CELERYBEAT_SCHEDULE = schedule_gen(['auckland','dunedin','onehunga','portchalmers'])
CELERYBEAT_SCHEDULE_FILENAME = '/var/lib/celery/celerybeat-schedule.db'
INSTALLED_APPS = ['tides.tasks']