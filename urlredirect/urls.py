"""urlredirect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import requests
from django.http import HttpResponse

def redirect_func(request,id):
    response = requests.get(f"https://afca-125-17-180-42.in.ngrok.io/get_image/{id}")
    print(response )
    return HttpResponse('ok')

def unsubscribe_redirect_func(request,email):
    response = requests.get(f"https://afca-125-17-180-42.in.ngrok.io/unsubscribe_mail/{email}")
    print(response )
    return HttpResponse('ok')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_image/<int:id>/',redirect_func),
    path('unsubscribe_mail/<str:email>',unsubscribe_redirect_func)
]
