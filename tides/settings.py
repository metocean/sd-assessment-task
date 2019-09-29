from celery.schedules import crontab

BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'
CELERY_RESULT_BACKEND = 'db+sqlite:////var/lib/celery/results.db'
CELERYBEAT_SCHEDULE = {
	'raglan_tide': {
        'task': 'tides.tasks.request_from_api',
        'schedule': crontab(minute='*'),
        'kwargs': {
        	'endpoint': 'https://tide.metoceanapi.com/',
        	'params': {},
        	'apikey': '',
        }
    },
}
CELERYBEAT_SCHEDULE_FILENAME = '//var/lib/celery/celerybeat-schedule'
INSTALLED_APPS = ['tides.tasks']