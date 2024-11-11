from django.contrib import admin
from .models import Flight

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'airline', 'code', 'departure', 'landing', 'duration')
    # You can also customize fieldsets to ensure proper display
    fields = ('origin', 'destination', 'airline', 'code', 'departure', 'landing', 'duration')

admin.site.register(Flight, FlightAdmin)