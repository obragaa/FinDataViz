# data_analyzer/urls.py
from django.urls import path
from . import views
from .views import stock_view, dashboard

urlpatterns = [
    # Exemplo de URL para uma página de índice
    path('', views.index, name='index'),
    path('stock/', stock_view, name='stock_view'),
    path('dashboard/', dashboard, name='dashboard'),
]
