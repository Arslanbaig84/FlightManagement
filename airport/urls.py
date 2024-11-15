from django.urls import path
from . import views

urlpatterns = [
    path('', views.airports, name='airports'),
    path('<str:code>', views.airport, name='airport'),
]