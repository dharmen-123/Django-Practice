from django.shortcuts import render
from .models import URLImage
from .forms import Imgform

# Create your views here.

def home(req):
    if req.method=='POST':
        form=Imgform(req.POST,req.FILES)
        if form.is_valid:
            form.save()
            form=Imgform()
            item=URLImage.objects.all()
            return render(req,'home.html',{'form':form,'data':item})
        else:
            item=URLImage.objects.all()
            return render(req,'home.html',{'form':form,'data':item})
    else :
        form=Imgform()
        item=URLImage.objects.all()
        return render(req,'home.html',{'form':form,'data':item})