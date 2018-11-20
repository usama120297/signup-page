from django.db import models
#from sign_up.models import Student

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
