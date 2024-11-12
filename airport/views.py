from django.shortcuts import render
from .models import Airport

# Create your views here.
def airports(request):
    airports = Airport.objects.all()
    return render(request, 'airport/index.html', {'airports':airports})