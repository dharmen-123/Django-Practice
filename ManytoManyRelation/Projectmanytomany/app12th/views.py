from django.shortcuts import render

# Create your views here.

from .models import Fuel, Vehicle

def home(req):
    ### Forward access #####
    vehicle= Vehicle.objects.get(id=1)
    x=vehicle.fuelname.all()
    for i in x:
        print(i.fuelname)

    ### Reverse access #####
    fuel = Fuel.objects.get(id=1)
    x=fuel.fuel.cars.all()
    print(fuel.fuelname)
    for i in x :
        print(i)
