from django.contrib import admin
from crudApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    student_list = ['sno','sname','date_of_birth','age','address']

admin.site.register(Student, StudentAdmin)


# Register your models here.
