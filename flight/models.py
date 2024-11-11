from django.db import models
from base.models import BaseModel
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from airport.models import Airport
from airline.models import Airline

# Create your models here.
class Flight(BaseModel):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flight_origins')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flight_destinations')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airline_flights')
    code = models.CharField(max_length=6, unique=True, validators=[
        RegexValidator(
            regex=r'^[A-Z]{2}\d{1,4}[A-Z]?$',
            message='Flight code must be in the format XX123 or XX123A',
        )
    ])
    departure = models.TimeField()
    landing = models.TimeField()
    capacity = models.PositiveSmallIntegerField()
    duration = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.origin} to {self.destination}'
    
    def save(self, *args, **kwargs):
        if self.origin != self.destination:
            super().save(*args, **kwargs)
        else:
            raise ValidationError('Origin and Destination cannot be the same')
