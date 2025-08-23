from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    contact=models.IntegerField()
    city=models.CharField()
    class Meta:
        db_table='Student'