from django.shortcuts import render, redirect

# Create your views here.
from .models import Student
def home(req):
     return render(req,'home.html')

def login(req):
    return render(req,'login.html')
    
def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # Check if user already exists
        if Student.objects.filter(email=email).exists():
            return render(request, 'login.html', {'error': 'Email already registered.'})

        # Check if passwords match
        if password == cpassword:
            Student.objects.create(
                name=name,
                email=email,
                password=password,
                cpassword=cpassword
            )
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
    return render(request, 'register.html')

def dashboard(req):
    return render(req,'dashboard.html')

def logindata(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        try:
            userdata = Student.objects.get(email=email)
        except Student.DoesNotExist:
            msg = "Email is not registered"
            return render(req, 'register.html', {'msg': msg})

        if password == userdata.password:
            data = {
                'id': userdata.id,
                'name': userdata.name,
                'email': userdata.email,
                'password': userdata.password,
                'cpassword': userdata.cpassword
            }
            # return render(req, 'dashboard.html', {'data': data})
            return redirect(dashboard)
        else:
            msg = "Email and password do not match"
            return render(req, 'login.html', {'msg': msg})
    
    return render(req, 'home.html')