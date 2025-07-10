from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,'home.html')

def designs(req):
    return render(req,'designs.html')

def about(req):
    return render(req,'about.html')

def services(req):
    return render(req,'services.html')

def login(req):
    return render(req,'login.html')

def register(req):
    return render(req,'register.html')