from django.shortcuts import render
from .models import GoogleSheet
from django.views.generic import View
from main.services.google_sheets_service import get_all_values
from main.services.requests_service import get_currency_rub


class MainView(View):
    def get(self, request):
        order_number_values, price_usd_values, delivery_time_values = get_all_values()
        currency = get_currency_rub()
        return render(request, 'main/main.html',
                      # {
                      #     'order_number': order_number_values,
                      #     'price_usd': price_usd_values,
                      #     'price_rub': currency,
                      #     'delivery_time': delivery_time_values,
                      #     'length_of_range': len(order_number_values)
                      # }
                      )
