from django.db import models

# Create your models here.

# class BaseInfo(models.Model):
#      name=models.CharField(max_length=50)
#      email=models.EmailField()
#      contact=models.IntegerField()
#      class Meta:
#         abstract = True

# class Employee(BaseInfo):
#      empid=models.IntegerField()
#      class Meta:
#            db_table='Employee'
#            verbose_name_plural='Employee'


# class Client(BaseInfo):
#      userid=models.IntegerField()
#      prject=models.CharField()
#      class Meta:
#            db_table='Client'
#            verbose_name_plural='Client'
           
##### Multitable model Inharitance

# class Basedata(models.Model):
#      name=models.CharField(max_length=50)
#      email=models.EmailField()
#      contact=models.IntegerField()
#      def __str__(self):
#         return self.name

# class Employe(Basedata):
#      empid=models.IntegerField()
#      salary=models.IntegerField()
#      def __str__(self):
#         return self.name
        
# class Student(Basedata):
#      Branch=models.CharField()
#      fees=models.IntegerField()
#      def __str__(self):
#         return self.name
                   
### Proxy Model Inharitance

class Basedata2(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField()
     contact=models.IntegerField()
     branch=models.CharField()
     fees=models.IntegerField()


class Proxy(Basedata2):
     class Meta:
        proxy=True
        ordering=['name']
