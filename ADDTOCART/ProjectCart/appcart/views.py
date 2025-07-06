from django.shortcuts import render

# Create your views here.
from .models import ItemInfo
def home(req):
    return render(req,'home.html')


def form(req):
    if req.method=='POST':
        itemname=req.POST.get('itemname')
        itemdes=req.POST.get('itemdes')
        itemprice=req.POST.get('itemprice')
        itemcolor=req.POST.get('itemcolor')
        itemimage=req.FILES.get('itemimage')
        ItemInfo.objects.create(itemname=itemname,itemdes=itemdes,itemprice=itemprice,itemimage=itemimage,itemcolor=itemcolor)
        return render(req,'admin.html')
    return render(req,'admin.html')
       

def user(req):
    itemdata=ItemInfo.objects.all()
    return render(req,'user.html',{'product':itemdata})
    

def adminlog(req):
    return render(req,'admin.html')
        
def addtocart(req,pk):
    
    return render(req,'addtocart.html',{'data':pk})
    