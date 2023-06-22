from django.shortcuts import render
from crudApp.models import Student
from crudApp.forms import StudentForm


# Create your views here.

def retrive_view(request):
    student = Student.objects.all()
    return render(request,'crudApp/index.html', {'student':student})

def add_student(request):
    form = StudentForm
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()     
    return render(request, 'crudApp/student_form.html', {'form':form})

