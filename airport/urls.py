from django.urls import path
from . import views

urlpatterns = [
    path('', views.airports, name='airports')
]