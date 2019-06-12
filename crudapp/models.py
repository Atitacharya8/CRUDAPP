from django.db import models


class Employee(models.Model):
    Eid = models.CharField(max_length=20)
    Ename = models.CharField(max_length=200)
    Eemail = models.EmailField()
    Econtact = models.CharField(max_length=15)

    class Meta:
        db_table="employee"



