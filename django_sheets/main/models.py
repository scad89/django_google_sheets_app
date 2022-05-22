from django.db import models


class GoogleSheet(models.Model):
    order_number = models.PositiveBigIntegerField(unique=True)
    price_usd = models.PositiveIntegerField()
    price_rub = models.FloatField()
    delivery_time = models.DateField()

    def __str__(self):
        return str(self.order_number)

    class Meta:
        verbose_name = 'Google Sheet'
        verbose_name_plural = 'Google Sheets'
