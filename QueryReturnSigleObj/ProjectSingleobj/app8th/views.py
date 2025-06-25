from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Student as Stu
def home(req):
     # data=Stu.objects.get(id=2)
     # print(data)
     # print(data.name,data.email,data.city,data.contact)

     # data2=Stu.objects.first()
     # data3=Stu.objects.last()


     # data4=Stu.objects.order_by('name').first()
     # data4=Stu.objects.order_by('name').last()

     # Stu.objects.create(name="Ravi",email='ravi@gamail.com',city='Satna',contact=9767798978)
     # data,create=Stu.objects.get_or_create(name="Yogesh",email='yogesh@gamail.com',city='Indore',contact=6978679148)
     # print(data)
     # print(create)

     # datadel=Stu.objects.get(id=8)
     # datadel.delete()

     d1=Stu.objects.filter(name='Raja')
     print(d1)
     # return  HttpResponse(data4)