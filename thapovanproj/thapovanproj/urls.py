"""thapovanproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
# from django.conf.urls import 

from thapovanapp import views as v1
from timeapp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('welcome/', v1.wish, name='Welcome'),
    # path('gm/', v1.gm_view, name="GM"),
    # path('ga/', v1.ga_view, name="GA"),
    # path('ge/', v1.ge_view, name="GE"),
    # path('time/', v2.get_time, name="time")   
    path('thapovanapp/', include('thapovanapp.urls')),
    path('timeapp/',include('timeapp.urls'))
]

# http://127.0.0.1:8000/timeapp/time


# print(__file__) - > to print file name 
# import os 
# print(os.path.abspath(__file__))  -----> toget absolute path file 
# print(os.path.dirname(os.path.abspath(__file__))) ------> to get directory name for abs path 

