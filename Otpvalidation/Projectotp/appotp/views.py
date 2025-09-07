from django.shortcuts import render,redirect
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return  render(request,'home.html')

def sendotp(request):

    send_mail(
                "Payment done", 
                "A successful payment is a transaction where a customer's payment method is successfully processed, resulting in the completion of a purchase or service. This means the customer's funds have been transferred to the recipient, and the transaction is finalized without any errors or issues. It's a critical indicator of a smooth checkout experience and directly impacts customer satisfaction and business revenue. ",
                "dharmendrachilhate11@gmail.com",
                ["harsh14thakre@gmail.com"],
                fail_silently=False,
    )
    return redirect('home')



