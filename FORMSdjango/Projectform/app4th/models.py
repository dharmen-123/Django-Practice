from django.db import models

# Create your models here.

class Student(models.Model):
    Stu_name =models.CharField(max_length=50)
    Stu_city=models.CharField(max_length=100)
    Stu_email=models.EmailField()
    Stu_contact=models.IntegerField()
    Stu_image=models.ImageField(upload_to='image/')
    Stu_document=models.FileField(upload_to='file/')