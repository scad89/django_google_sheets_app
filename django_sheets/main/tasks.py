from django_sheets.celery import app
from .models import GoogleSheet
from main.services.google_sheets_service import get_all_values
from main.services.celery_service import record_data, reset_primary_key
from celery.utils.log import get_task_logger
from dotenv import load_dotenv

load_dotenv()

logger = get_task_logger(__name__)


@app.task(bind=True)
def insert_data_to_bd(self):
    GoogleSheet.objects.all().delete()
    reset_primary_key()
    order_number, price_usd, delivery_time = get_all_values()
    record_data(order_number, price_usd, delivery_time)
    return logger.info(f'Data recorded to the database')
