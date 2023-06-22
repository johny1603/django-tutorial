import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'templateDemo.settings')
import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        fsno = randint(1001, 9999)
        fsname = faker.name()
        fdob = faker.date()
        fage = randint(21,50)
        fsaddress = faker.city()
        stud_record = Student.objects.get_or_create (sno=fsno, sname =fsname, date_of_birth=fdob,
                                                age = fage, address=fsaddress)
populate(20)