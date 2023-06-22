from django.shortcuts import render
from django.http import HttpResponse
from dbApp.models import Employee

# Create your views here.

def emp_details(request):
    emp_data = Employee.objects.all()
    emp_dict = {'emp_list':emp_data}
    return render(request, 'dbApp/employee.html', context=emp_dict)
    # return HttpResponse("Employee details shared")
