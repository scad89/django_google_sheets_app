from django.shortcuts import render
from .models import GoogleSheet
from django.views.generic import View
from main.services.google_sheets_service import get_all_values
from main.services.requests_service import get_currency_rub
from django.db.models import Sum


class MainView(View):
    def get(self, request):
        all_data_from_db = GoogleSheet.objects.all()
        return render(request, 'main/main.html',
                      {
                          'data': all_data_from_db,
                      }
                      )
