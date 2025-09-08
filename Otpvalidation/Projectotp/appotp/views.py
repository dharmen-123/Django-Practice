from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
import random
# Create your views here.

def home(request):
    return  render(request,'home.html')

def generate(request):
    return str(random.randint(100000,999999))

def sendotp(request):
    if request.method=='POST':
        email=request.POST.get('email')
        otp=generate(request)
        request.session['otp']=otp
        send_mail(
            "Payment done", 
            f"This is your Register otp {otp} ",
            "dharmendrachilhate11@gmail.com",
            [email],
            fail_silently=False,
        )
        return render(request,'home.html',{'email':email})

def register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        userotp=request.POST.get('otp')
        sendotp=request.session.get('otp')
        if userotp == sendotp:
            if 'otp' in request.session:
                del request.session['otp']
            messages.success(request,'Registration successfull')
            return redirect('home')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('home')
    return render(request,'home.html')
