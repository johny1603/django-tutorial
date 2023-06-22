from django.db import models

# Create your models here.

# inheritance
# An object of one class behaving as an object of another class

class Employee(models.Model):
    
    empNo = models.CharField(max_length=100)
    empName = models.CharField(max_length=100)
    empSalary = models.IntegerField()
    empAddress = models.CharField(max_length=100)


def __str__(self):
    return "Employee details shared"

