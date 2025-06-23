from django.shortcuts import render

# Create your views here.

from .models import Student as Stu

def home(self):
    all_data=Stu.objects.all()
    print(all_data)
    print(all_data.values_list())
