from django.db import models
from base.models import BaseModel
from django.core.validators import RegexValidator

# Create your models here.
class Airline(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=2, unique=True, validators=[
        RegexValidator(
            regex=r'^[A-Z]{2}$',
            message='Airline code must be exactly two uppercase letters (IATA standard)')
            ]
        )
    origin = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    

class Airport(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    city_name = models.CharField(max_length=150)
    code = models.CharField(max_length=3, unique=True, validators=[
        RegexValidator(
            regex=r'^[A-Z]{3}$',
            message='Airline code must be exactly three uppercase letters (IATA standard)')
            ]
        )
    def __str__(self) -> str:
        return f'{self.name} ({self.code})'