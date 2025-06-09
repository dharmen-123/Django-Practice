from django.shortcuts import render , redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json
from django.urls import reverse
from urllib.parse import urlencode 
print("views.py")

# def home(request):
#     # return HttpResponse("<h1 style='color:red','fontSize:30px'>This is Home page...........</h1>")
#     data=[{"name":"dharmendra", "age":20},{"name":"Harsh", "age":20},{"name":"Viplove", "age":22}]
#     data1={"name":"dharmendra", "age":20}
#     # jdata= json.dumps(data)
#     # return HttpResponse(jdata, content_type='application/json')

#     return JsonResponse(data ,safe=False)
#     # return JsonResponse(data1)

# def about(request):
#     # return HttpResponse("<h1 style='color:red','fontSize:30px'>This is About page...........</h1>")
#       return redirect() 
# def contact(request):
#     return HttpResponse("<h1 style='color:red','fontSize:30px'>This is Contact page...........</h1>")
    
# def services(request):
#     return HttpResponse("<h1 style='color:red','fontSize:30px'>This is Servicer page...........</h1>")


# def myrender(req):
#     context={'name':"Python"}
#     return render(req, "home.html", context)

# def myrender(req):
#       context={"name":"dharmendra"}
#       response=render(req, "home.html", context)
#       return response


# def about(req):
#     # return render(req,'home.html', context=None)
#     return redirect('home',"dharmendra")

def about(req):
    base_url=reverse('redirect1')
    query_string = urlencode({'name':'Dharmendra','age':20})
    return redirect(f'{base_url}?{query_string}')

# def home(req,x):
#     context={}
#     context['first']=x
#     return render(req,'home.html', context)

def redirect1(req):
    print(req.method)
    print(req.GET)
    print(req.POST)
    print(req.META)
    print(req.COOKIES)