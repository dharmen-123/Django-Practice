"""
URL configuration for ProjectCart project.

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from appcart import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('user/',views.user,name='user'),
    path('adminlog/',views.adminlog,name='adminlog'),
    path('cart/',views.cart,name='cart'),
    path('remove/<int:rid>/',views.remove,name='remove'),
    path('addtocart/<int:pk>/',views.addtocart,name='addtocart'),
    path('payment/',views.payment,name='payment'),
    path('paymenthandler/',views.paymenthandler,name='paymenthandler'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

