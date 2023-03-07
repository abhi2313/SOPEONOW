from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here .



class Post(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    date_of_joining=models.DateField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    active=models.BooleanField()
    leave_count=models.IntegerField()
    on_leave=models.BooleanField()
    def __str__(self):
        return self.name
   



    

