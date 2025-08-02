from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length = 50)
    email=models.EmailField()
    password=models.CharField(max_length = 50)
    cpassword=models.CharField(max_length = 50)
    def _str_(self):
        return self.name

class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField()
    query=models.CharField()