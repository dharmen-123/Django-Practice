from django.db import models

# Create your models here.

class ItemInfo(models.Model):
    itemname=models.CharField(max_length=100)
    
