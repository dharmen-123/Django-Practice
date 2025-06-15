from django.shortcuts import render

# Create your views here.

from .forms import StudentForm


def home(req):
    form=StudentForm()
    return render(req,'home.html',{'fm':form})

def data(req):
    return render(req,'data.html')