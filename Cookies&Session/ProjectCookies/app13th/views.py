from django.shortcuts import render

# Create your views here.

def set(req):
    data=render(req,'set.html')
    data.set_cookie('name',"Dharmendra",max_age=60*60,httponly=True,secure=True)
    data.set_cookie('city',"Bhopal",max_age=60*60,httponly=True,secure=True)
    data.set_cookie('branch',"AIML",max_age=60*60,httponly=True,secure=True)

    return data

def get(req):
    name=req.COKKIES['name']
    city=req.COKKIES['city']
    branch=req.COKKIES['branch']
    
    print(name)
    print(city)
    print(branch)
    details={
        'name':name,'city':city,'branch':branch
    }
    return render(req,'get.html',{'data':details})

def delete(req):
    data = render(req,'set.html')
    data.delete_cookie('name')
    data.delete_cookie('city')
    data.delete_cookie('branch')
    return data