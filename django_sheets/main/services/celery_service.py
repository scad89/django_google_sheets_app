from ..models import GoogleSheet
from main.services.requests_service import get_currency_rub
from django.core.management.color import no_style
from django.db import connection


def reset_primary_key():
    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [GoogleSheet])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)


def record_data(order_number, price_usd, delivery_time):
    currency = get_currency_rub()
    return GoogleSheet.objects.bulk_create([
        GoogleSheet(
            order_number=order_number[i],
            price_usd=int(price_usd[i]),
            price_rub=round(int(price_usd[i])*currency, 2),
            delivery_time='-'.join(delivery_time[i].split('.')[::-1])
        )
        for i in range(len(order_number))
    ])
