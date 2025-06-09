from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html')


def data(request):
    if request.method=="POST":
         p=request.POST.get('a')
         q=request.POST.get('b')
         r=request.POST.get('c')
         s=request.FILES.get('d')
         t=request.FILES.get('e')
    #      print(p,q,r,s,t)
    # print(request.POST)
    # print(request.FILES)
    # print(request.method)
         data={
             'name':p,
             'email':q,
             'contact':r,
             'image':s,
             'resume':t
         }
         return  render(request, 'data.html', {'key':data})