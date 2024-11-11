from django.urls import path
from . import views

urlpatterns = [
    path('', views.airlines, name='airlines')
]