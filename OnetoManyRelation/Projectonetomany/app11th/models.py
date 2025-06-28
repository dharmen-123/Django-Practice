from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name=models.CharField(max_length=100, unique=True)
    dep_datail=models.CharField()
    def __str__(self):
        return self.dep_name

class Student(models.Model):
    Stuname= models.CharField(max_length=100)
    Stuemail= models.EmailField()
    Stucontact = models.IntegerField()
    Stu_dep = models.ForeignKey(Department,on_delete=models.PROTECT,to_field='dep_name',related_name='student_data')
    def __str__(self):
        return self.Stuname
