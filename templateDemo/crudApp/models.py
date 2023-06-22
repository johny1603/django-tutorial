from django.db import models

# Create your models here.

class Student(models.Model):
    sno = models.CharField(max_length=50)
    sname = models.CharField(max_length=50,null=False)
    date_of_birth = models.DateField(null=False)
    age = models.IntegerField()
    # student_image = models.ImageField()
    address= models.CharField(max_length=500)

    def __str__(self):
        return(self.sname)






