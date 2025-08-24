from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Student

# Create your views here.

def home(request):
    return HttpResponse("Hello python ..................")


### CRUD Operation on shell ########

##<-------- Create ------------------>
# Student.objects.create(name="name",email="email",........)
##  or
# a=Student(name="name",email="email",............)
# a.save()

## <------------ Read ----------->
# data=Student.objects.all()
# print(data)
#    OR
# Student.objects.values()

## <----------- Update ------------>
#  a=Student.objects.get(id=2)
# a.name=newname
#a.save()






