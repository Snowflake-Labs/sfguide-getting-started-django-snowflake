from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Trip

# Create your views here.

def index(request):
    return HttpResponse("Hello there! Welcome to the django-snowflake Quickstart!")

class GrahamConselyeaView(generic.ListView):
    template_name = 'trips/trips-from-graham-conselyea.html'
    context_object_name = 'trip_list'

    def get_queryset(self):
        """Return the last 10 trips from the 'Graham Ave & Conselyea St' Citibike station."""
        return Trip.objects.filter(start_station_name='Graham Ave & Conselyea St')[:10]