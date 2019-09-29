from __future__ import absolute_import

from celery import Celery

from . import settings

app = Celery('tides')
app.config_from_object(settings)

from . import tasks
