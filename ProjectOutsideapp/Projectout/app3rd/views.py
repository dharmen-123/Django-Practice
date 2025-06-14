from django.shortcuts import render
# Create your views here.

def home(req):
    if req.method=="POST":
         p=req.POST.get('a')
         q=req.POST.get('b')
         r=req.POST.get('c')
         s=req.FILES.get('d')
         t=req.FILES.get('e')
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

         data2={'name':"Dharmendra",'age':20,'branch':"AIML",'contact':987867565}
         return  render(req, 'home.html', {'key2':data2,'key':data})
    return render(req, 'home.html')


# def data(request):
    # if request.method=="POST":
    #      p=request.POST.get('a')
    #      q=request.POST.get('b')
    #      r=request.POST.get('c')
    #      s=request.FILES.get('d')
    #      t=request.FILES.get('e')
    # #      print(p,q,r,s,t)
    # # print(request.POST)
    # # print(request.FILES)
    # # print(request.method)
    #      data={
    #          'name':p,
    #          'email':q,
    #          'contact':r,
    #          'image':s,
    #          'resume':t
    #      }
    #      return  render(request, 'home.html', {'key':data})
         