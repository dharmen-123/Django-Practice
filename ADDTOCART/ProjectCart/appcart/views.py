from django.shortcuts import render

# Create your views here.
from .models import ItemInfo
def home(req):
    return render(req,'home.html')

def register(req):
    return render(req,'register.html')

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
    if req.method=='POST':
        quantity=req.session.get('quantity',[])
        cart=req.session.get('cart',[])
        qua=int(req.POST.get('quantity'))
        quantity.append(qua)
        cart.append(pk)
        req.session['quantity']=quantity
        req.session['cart']=cart
        itemdata=ItemInfo.objects.all()
        return render(req,'user.html',{'product':itemdata})
    return render(req,'user.html')
    
def cart(req):
    cart=req.session.get('cart',[])
    quantity=req.session.get('quantity',[])
    # print(cart, quantity)
    # return render(req,'addtocart.html') 
    l=[]
    totalprice=0
    for i in cart:
        data = {
            'name':i.itemname,
            'des':i.itemdes,
            'price':i.itemprice,
            'color':i.itemcolor,
            'image':i.itemimage
        }
        totalprice+=i.itemprice
        l.append(data)
    return render(req,'addtocart.html',{listdata:l})