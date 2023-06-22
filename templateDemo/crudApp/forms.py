from django.contrib import admin
from django import forms
from crudApp.models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['sno']
        # exclude = ['sno'] if no need the fields inthe form we have to use exclude


#data -->contain of information
# Meta data ---> data about data
# ex : email ===> sender/ ip/network provider/ time/ browser




