import logging

from celery import shared_task
from django.core.management import call_command

logger = logging.getLogger(__name__)


@shared_task(
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=600,
    max_retries=5,
)
def download_weather_data_task():
    """Celery task for downloading weather data from IMGW with exponential backoff retries."""
    logger.info("Executing download_weather_data_task...")
    call_command('fetch_weather')