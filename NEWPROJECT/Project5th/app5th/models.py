from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length = 50)
    email=models.EmailField()
    detail=models.CharField(max_length = 50)
    phone=models.IntegerField()
    education=models.CharField(max_length = 50)
    gender=models.CharField(max_length = 50)
    dob=models.DateField()
    profile_pic=models.ImageField(upload_to = 'image/')
    resume=models.FileField(upload_to = 'file/')
    password=models.CharField(max_length = 50)
    def _str_(self):
        return self.name