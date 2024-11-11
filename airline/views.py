from django.shortcuts import render
from flight.models import Flight
from .models import Airline

# Create your views here.
def airlines(request):
    dataairlines = Airline.objects.all()
    return render(request, 'airline/index.html', {'dataairlines':dataairlines})