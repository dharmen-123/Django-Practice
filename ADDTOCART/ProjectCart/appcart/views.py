from django.shortcuts import render,redirect
from django.contrib import messages 
# Create your views here.
from .models import ItemInfo
def home(req):
    cart=req.session.get('cart',[])
    count=len(cart)
    return render(req,'home.html',{'count':count})

def register(req):
    cart=req.session.get('cart',[])
    count=len(cart)
    return render(req,'register.html',{'count':count})

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
    cart=req.session.get('cart',[])
    count=len(cart)
    itemdata=ItemInfo.objects.all()
    return render(req,'user.html',{'product':itemdata,'count':count})
    

def adminlog(req):
    return render(req,'admin.html')

# def addtocart(req,pk):
#     if req.method=='POST':
#         cart=req,session.get('cart',{})
        

def addtocart(req,pk):
    cart=req.session.get('cart',[])
    count=len(cart)
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
        return render(req,'user.html',{'product':itemdata,'count':count})
    return render(req,'user.html',{'count':count})
    
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
        count=len(l)
    return render(req,'addtocart.html',{'listdata':l,'totalprice':totalprice,'count':count})

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
    if req.method=='POST':
        amount=req.POST.get('amount')*100

    client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))
    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    pass