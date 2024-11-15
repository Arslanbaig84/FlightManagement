from django.shortcuts import render
from flight.models import Flight

# Create your views here.
def flights(request):
    flights = Flight.objects.all()
    return render (request, 'flight/index.html', {'flights': flights})


def flight(request, code):
    flight = Flight.objects.get(code=code)
    return render(request, 'flight/flight.html', {'flight':flight})