import os
from celery import Celery

# Main file for celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('WeatherPulseApi')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()