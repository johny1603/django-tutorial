from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def wish(request):
    message = """<h1>Hi Buddy welcome to website</h1>
                    <h2> coming soon the website....</h2>"""
    
    return HttpResponse(message)
    

def gm_view(request):
     message = """<h1>Hi Good morning</h1>
                    <h2> Have a good day....</h2>"""
     return HttpResponse(message)

def ga_view(request):
     message = """<h1>Hi Good Afternoon</h1>
                    <h2> Have a good day....</h2>"""
     return HttpResponse(message)

def ge_view(request):
     message = """<h1>Hi Good Evening</h1>
                    <h2> Have a good day....</h2>"""
     return HttpResponse(message)



# django server install
# django projects
# start app
#  project --> settings --> app callable
# views .py return response

