from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def get_time(request):
    time = datetime.now()
    result = '<h1> The time is :'+ str(time)+ '</h1>'
    return HttpResponse(result)

# Create your views here.
