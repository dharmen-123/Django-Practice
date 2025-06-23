from django.shortcuts import render

# Create your views here.

from .models import Student as Stu

def home(self):
    all_data=Stu.objects.all()
    print(all_data)
    for i in all_data:
        print(i.name)
        print(i.email)
        print(i.contact)
        print(i.city)
    print(all_data.values_list())
