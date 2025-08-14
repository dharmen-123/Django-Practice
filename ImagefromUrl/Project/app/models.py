from django.db import models

# Create your models here.

class URLImage(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField()
    
    class Meta:
        db_table='URLImage'