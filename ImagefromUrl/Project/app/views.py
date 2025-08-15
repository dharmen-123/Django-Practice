from django.shortcuts import render,redirect
from .models import URLImage
# from .forms import Imgform
import json

# Create your views here.

# def home(req):
#     if req.method=='POST':
#         form=Imgform(req.POST,req.FILES)
#         if form.is_valid:
#             form.save()
#             form=Imgform()
#             item=URLImage.objects.all()
#             return render(req,'home.html',{'form':form,'data':item})
#         else:
#             item=URLImage.objects.all()
#             return render(req,'home.html',{'form':form,'data':item})
#     else :
#         form=Imgform()
#         item=URLImage.objects.all()
#         return render(req,'home.html',{'form':form,'data':item})


def upload_images(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        urls = request.POST.getlist('image_url')  # Collect all inputs named "image_url"
        URLImage.objects.create(name=name, image_urls=urls)
        return redirect('gallery')  # Replace with your success page or message
    return render(request, 'upload_images.html')


def gallery_view(request):
    all_entries = URLImage.objects.all()

    # Ensure image_urls is a Python list for each entry
    for entry in all_entries:
        if isinstance(entry.image_urls, str):
            entry.image_urls = json.loads(entry.image_urls)

    return render(request, 'upload_images.html', {'entries': all_entries})

from django.db.models import Q

def search(req):
    sdata=req.POST.get('search')
    # userdata=URLImage.objects.get(id=pk)
    all_entries=URLImage.objects.filter(Q(name__icontains=sdata))
    for entry in all_entries:
        if isinstance(entry.image_urls, str):
            entry.image_urls = json.loads(entry.image_urls)

    return render(req, 'upload_images.html', {'entries': all_entries})
