from django.shortcuts import render

# Create your views here.
from .models import  Student as Stu

def home(req):
    # all_data=Stu.objects.all().values()
    # # print(all_data.values_list)
    # # for i in all_data:
    # #     print(i)

    # second=Stu.objects.filter(name='Viplove')
    # # print(second)

    # third=Stu.objects.order_by('name')


    # fourth = Stu.objects.exclude(name='Dharmendra')

    # return render(req,'home.html',{'data':all_data,'data2':second ,'data3':third,'data4':fourth})

    firstdata=Stu.objects.all()[:5]

    lastdata=Stu.objects.all()[::-1][:5] 
    # last=(list(reversed(lastdata)))[:5]
    # print(last)
    return render(req,'home.html',{'data':firstdata,'data2':lastdata})