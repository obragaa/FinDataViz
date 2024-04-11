# data_analyzer/views.py
from django.shortcuts import render
from .api import get_stock_data  # Função da API
import requests

def stock_view(request):
    symbol = 'IBM'  # Exemplo de símbolo de ação
    data = get_stock_data(symbol)
    # Estrutura os dados para iteração no template
    time_series = data.get("Time Series (Daily)", {})
    daily_data_list = [
        {'date': date, 'close': info.get("4. close")} for date, info in time_series.items()
    ]
    # Extraia o símbolo da ação diretamente aqui
    stock_symbol = data.get("Meta Data", {}).get("2. Symbol", "Unknown Symbol")
    # Passe o símbolo e os dados diários para o template
    context = {
        'daily_data_list': daily_data_list,
        'stock_symbol': stock_symbol
    }
    return render(request, 'data_analyzer/stock.html', context)

def index(request):
    # Aqui, eventualmente, você vai chamar a API e passar os dados para o template
    return render(request, 'data_analyzer/index.html', {})

def fetch_stock_data(symbol):
    API_KEY = '2AFK71GUDN5JCXWC'
    BASE_URL = 'https://www.alphavantage.co/query'
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Verifique se a chave 'Meta Data' existe antes de acessá-la
    if 'Meta Data' not in data:
        print("Meta Data not found in API response")
        return [], [], None  # Retorna listas vazias para datas e preços e None para last_refresh

    last_refresh = data['Meta Data']['3. Last Refreshed']
    time_series = data['Time Series (Daily)']
    dates = sorted(time_series.keys(), reverse=True)[:5]  # Últimos 5 dias
    prices = [time_series[date]['4. close'] for date in dates]

    return dates, prices, last_refresh


def dashboard(request):
    dates, prices, last_refresh = fetch_stock_data("AAPL")
    context = {
        'stock_symbol': 'AAPL',
        'last_refresh': last_refresh,
        'dates': dates,
        'prices': prices
    }
    return render(request, 'data_analyzer/dashboard.html', context)
