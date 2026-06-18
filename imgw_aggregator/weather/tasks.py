from celery import shared_task
from django.core.management import call_command

@shared_task
def download_weather_data_task():
    """Celery task for downloading weather data from IMGW"""
    call_command('fetch_weather')