from django.db import models

# Create your models here.

class BaseInfo(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     contact=models.IntegerField()
     class Meta:
        abstract = True

class Employee(BaseInfo):
     empid=models.IntegerField()


class Client(BaseInfo):
     userid=models.IntegerField()
     prject=models.CharField()
