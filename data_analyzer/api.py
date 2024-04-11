#XANJCCH7LU1H0ZN2
# data_analyzer/api.py
import requests

def get_stock_data(symbol):
    API_KEY = 'XANJCCH7LU1H0ZN2'
    BASE_URL = 'https://www.alphavantage.co/query'

    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Processamento dos dados pode ser feito aqui
    return data