from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime


# Create your views here.

def display_login(request):
    message = "Hi"
    date = datetime.now()
    hour = int(date.strftime('%H'))
    if hour < 12:
        message += " Good Morning"
    else:
        message += " Good Evening"
    emp_name ="John Britto"
    display_date = {'date':date,'emp_name':emp_name,'greeting':message}
    return render(request, 'templateapp/abc.html', context = display_date)
    # return render(request, 'templateapp/first.html', context = display_date)
