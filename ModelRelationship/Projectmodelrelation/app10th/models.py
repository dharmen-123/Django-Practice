from django.db import models

# Create your models here.

class Addhar(models.Model):
    aadhar=models.IntegerField(unique=True)
    createdate=models.DateTimeField()
    createby=models.CharField(max_length=20)
    def __str__(self):
        return str(self.aadhar)

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    addhar_no=models.OneToOneField(Addhar,on_delete=models.PROTECT,to_field='aadhar',related_name='student_info')
    def __str__(self):
        return self.name

