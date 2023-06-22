from django.shortcuts import render

# Create your views here.

def getcookieInfo(request):
    count  = request.COOKIES.get('count',0)
    totalCount = int(count) + 1
    # expiry_date = request.COOKIES.get_expiry_date()
    response =  render(request, 'sessionApp/cookie.html', {'count':totalCount})

    response.set_cookie('count', totalCount)
    return response

def getSessionInfo(request):
    count  = request.session.get('count',0)
    totalCount = int(count) + 1
    request.session['count'] = totalCount
    expiry_date = request.session.get_expiry_date()
    cookie_age = request.session.get_session_cookie_age()
    session_data = {'count': totalCount,'expiry_date':expiry_date, 'age':cookie_age}
    return render (request, 'sessionApp/session.html',context=session_data)