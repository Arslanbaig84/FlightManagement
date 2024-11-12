from django.shortcuts import render
from flight.models import Flight

# Create your views here.
def flights(request):
    flights = Flight.objects.all()
    return render (request, 'flight/index.html', {'flights': flights})