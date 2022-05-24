import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_sheets.settings')

app = Celery('django_sheets')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
