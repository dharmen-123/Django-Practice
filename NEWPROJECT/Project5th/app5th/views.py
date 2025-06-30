from django.shortcuts import render, redirect

# Create your views here.
from .models import Student
def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def services(req):
    return render(req,'services.html')

def login(req):
    return render(req,'login.html')


def register(request):
    if request.method=="POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        detail = request.POST.get('detail')
        phone = request.POST.get('phone')
        education = request.POST.getlist('subscribe')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        profile_pic = request.FILES.get('profile-pic')
        resume = request.FILES.get('resume')
        user = Student.objects.filter(email=email)
        if user:
            return render( request,'register.html') 
        else:
            if password == cpassword:
                Student.objects.create(name=name,email=email,detail=detail,phone=phone,education=education,gender=gender,dob=dob,profile_pic=profile_pic,resume=resume,password=password)
                return redirect('login')

            else:
                return redirect('register')
    else:
        return render(request,'register.html')

def logindata(req):
    if req.method=="POST":
        email = req.POST.get('email')
        password = req.POST.get('password')
        data=Student.objects.filter(email=email)
        if data:
           print("hello.......")
           userdata=Student.objects.get(email=email)
           pass1=userdata.password
           if password==pass1:
                data={
                'id':userdata.id,   
                'name': userdata.name,  
                'email': userdata.email , 
                'detail': userdata.detail,
                'phone': userdata.phone  ,
                'education': userdata.education,
                'gender': userdata.gender  ,
                'dob': userdata.dob  ,
                'password': userdata.password,  
                'profile_pic': userdata.profile_pic,  
                'resume': userdata.resume 
                }    
                return render(req,'dashboard.html',{'data':data})
           else :
              msg="Email and password is not matched"
              return render(req,'login.html',{'msg':msg})
        else:
            msg="Email is not registered"
            return render(req,'register.html',{'msg':msg})
    else:
        return render(req,'home.html')

def dashboard(req):
     return render(req,'dashboard.html')
     

def query(req,pk):
     userdata=Student.objects.get(id=pk)
     