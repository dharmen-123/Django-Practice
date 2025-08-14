from django.shortcuts import render,redirect
from django.contrib import messages 
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

# def addtocart(req,pk):
#     if req.method=='POST':
#         cart=req,session.get('cart',{})
        

def addtocart(req,pk):
    if req.method=='POST':
        quantity=req.session.get('quantity',[])
        cart=req.session.get('cart',[])
        qua=int(req.POST.get('quantity'))  
        if pk not in cart: 
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
    l=[]
    totalprice=0
    for i,j in zip(cart,quantity):
        i=ItemInfo.objects.get(id=i)
        data = {
            'id':i.id,
            'name':i.itemname,
            'des':i.itemdes,
            'price':i.itemprice,
            'color':i.itemcolor,
            'image':i.itemimage,
            'quantity':j,
            'total':i.itemprice*j
        }
        totalprice+=i.itemprice*j
        l.append(data)
    return render(req,'addtocart.html',{'listdata':l,'totalprice':totalprice})

def remove(req,rid):
    cart=req.session.get('cart',[])
    quantity=req.session.get('quantity',[])
    print(rid)
    print(type(rid))
    # r=str(rid)
    rindex=cart.index(rid)
    if rid in cart:
        del cart[rindex]
        del quantity[rindex]
        req.session['cart'] = cart
        req.session['quantity'] = quantity
        req.session.modified=True   
        return  redirect('cart')  
    else:
        return  redirect('cart')  
    
def login(req):
    return render(req,'login.html')

def payment(req):
    pass