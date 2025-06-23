from django.db import models

# Create your models here.
class Student(models.Model):
     name= models.CharField(max_length=50)
     email= models.EmailField()
     contact= models.IntegerField()
     city= models.CharField(max_length=70)
     
