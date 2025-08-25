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

### <------------- Delete ----------------->
# d=Student.objects.get(id=idnumber)
# d.delete()

### <----------- Bulk Update -------------->
# a=Student.objects.filter(colonname=colonvalue).update(colonname=newvalue)

## <------- Check the objects method and attributes
# d1 = Student.objects.get(id=1)
# dir(d1) it has approx 97 methods 

## CRUD Methods
# 1. GET 
# 2. POST 
# 3. PUT 
# 4. PATCH 
# 5. DELETE

# CRUD with Cloudnary




