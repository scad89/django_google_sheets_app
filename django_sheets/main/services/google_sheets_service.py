from locale import currency
from pprint import pprint
import os
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from main.services.requests_service import get_currency_rub
from dotenv import load_dotenv

load_dotenv()


def get_values_from_sheet():
    basedir = os.path.abspath(os.path.dirname(__file__))
    CREDENTIALS_FILE = basedir+'/creds.json'
    spreadsheet_id = "1LrFj3Q8E_rcNCI3hGAA7qXm31mNQO8tJli7ThE8SuNg"
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A2:E100',
        majorDimension='COLUMNS'
    ).execute()
    return values


def get_all_values():
    values = get_values_from_sheet()
    order_number_values = tuple(values['values'][1])
    price_usd_values = tuple(values['values'][2])
    delivery_time_values = tuple(values['values'][3])
    return order_number_values, price_usd_values, delivery_time_values
