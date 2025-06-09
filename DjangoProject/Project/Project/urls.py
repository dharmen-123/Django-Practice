"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
print("urls.py")

from django.contrib import admin
from django.urls import path

from Myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.about, name='about'),
    # path('home/<int:x>/', views.home,name='home'),
    # path('home/<str:x>/', views.home,name='home'),
    # path('home/<slug:x>/', views.home,name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('myrender/',views.myrender, name='myrender' ),
    path('redirect1', views.redirect1, name='redirect1'),
]
