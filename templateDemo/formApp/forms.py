from django.contrib import admin
from django import forms

class EmployeeInfoForm(forms.Form):
    name = forms.CharField()
    salary = forms.IntegerField()
    age = forms.IntegerField()