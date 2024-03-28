from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    sal = models.FloatField()
