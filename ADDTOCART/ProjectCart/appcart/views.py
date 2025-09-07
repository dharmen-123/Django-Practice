from django.shortcuts import render,redirect
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponseBadRequest
import razorpay
from .models import ItemInfo,Payment
from django.core.mail import send_mail


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
        cart=req.session.get('cart',[])
        count=len(cart)
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
            'im  age':i.itemimage,
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


@csrf_exempt
def payment(req):
    
    print("hello")
    if req.method == "POST":
        # try:
            print("hello")
            amount = int(req.POST.get('amount')) * 100  # Convert to paise
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            order_data = {
                "amount": amount,
                "currency": "INR",
                "receipt": "order_rcptid_11",
                "payment_capture": 1
            }
            order = client.order.create(data=order_data)
            Payment.objects.create(
            order_id=order["id"],
            amount=amount,
            status="Created"
            )
            payment = {
                "order_id": order["id"],
                "amount": amount,
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "currency": "INR",
                "callback_url": "/paymenthandler/"
            }
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
                    'im  age':i.itemimage,
                    'quantity':j,
                    'total':i.itemprice*j
                }
                totalprice+=i.itemprice*j
                l.append(data)
            count=len(l)
            return render(req,'addtocart.html',{'listdata':l,'payment':payment,'totalprice':totalprice,'count':count})
    return render(req, "addtocart.html", {'payment': None})

@csrf_exempt
def paymenthandler(request):
    print("hello.......")
    if request.method == "POST":
        print("hello.......")

        try:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            params_dict = {
                'razorpay_order_id': request.POST.get('razorpay_order_id'),
                'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                'razorpay_signature': request.POST.get('razorpay_signature')
            }
            client.utility.verify_payment_signature(params_dict)
            payment = Payment.objects.get(order_id=request.POST.get('razorpay_order_id'))
            payment.payment_id = request.POST.get('razorpay_payment_id')
            payment.signature = request.POST.get('razorpay_signature')
            payment.status = "Paid"
            payment.save()
            send_mail(
                "Payment done", 
                "A successful payment is a transaction where a customer's payment method is successfully processed, resulting in the completion of a purchase or service. This means the customer's funds have been transferred to the recipient, and the transaction is finalized without any errors or issues. It's a critical indicator of a smooth checkout experience and directly impacts customer satisfaction and business revenue. ",
                "dharmendrachilhate11@gmail.com",
                ["dharmendrachilhate11@gmail.com"],
                fail_silently=False,
            )
            return redirect('home')

        except razorpay.errors.SignatureVerificationError:
            return redirect('home')
    return HttpResponseBadRequest("Invalid request")
