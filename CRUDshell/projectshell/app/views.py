from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Student

def home(request):
    return HttpResponse("Hello python ..................")
    