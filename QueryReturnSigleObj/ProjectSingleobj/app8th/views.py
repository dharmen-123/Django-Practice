from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Student as Stu
def home(req):
     data=Stu.objects.get(id=2)
     print(data)
     print(data.name,data.email,data.city,data.contact)
     return  HttpResponse(data)