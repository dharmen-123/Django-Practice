from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    email=models.EmailField()
    password=models.CharField()

    class Meta:
        db_table='Student'