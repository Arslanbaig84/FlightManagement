from django.urls import path
from . import views

urlpatterns = [
    path('', views.flights, name='flights'),
    path('<str:code>/', views.flight, name='flight'),
]