from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    # Show flights in the past
    cars = Car.objects.all()
    context = {'car_list': cars, 'app_name': 'carRentalApp'}
    return render(request, 'index.html', context)

def details(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    context = {'car_data': car, 'app_name': 'carRentalApp'}
    return render(request, 'details.html', context)