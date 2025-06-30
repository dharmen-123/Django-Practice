from django.db import models

# Create your models here.

class Fuel(models.Model):
    fuelname=models.CharField(max_length=200)
    def __str__(self):
        return self.fuelname

class Vehicle(models.Model):
    carname=models.CharField(max_length=200)
    fuelname=models.ManyToManyField(Fuel,related_name="cars")
    def __str__(self):
        return self.carname
        