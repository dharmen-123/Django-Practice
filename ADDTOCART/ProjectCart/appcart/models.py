from django.db import models

# Create your models here.

class ItemInfo(models.Model):
    itemname=models.CharField(max_length=100)
    itemdes=models.CharField()
    itemprice=models.IntegerField()
    itemimage=models.ImageField(upload_to='file')
    itemcolor=models.CharField()
    


