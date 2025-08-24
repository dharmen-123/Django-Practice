from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Student

# Create your views here.

def home(request):
    return HttpResponse("Hello python ..................")
