from django.shortcuts import render
from flight.models import Flight
from .models import Airline

# Create your views here.
def airlines(request):
    airlines = Airline.objects.all()
    return render(request, 'airline/index.html', {'airlines':airlines})

def airline(request, code):
    airline = Airline.objects.get(code=code)
    return render(request, 'airline/airline.html', {'airline':airline})