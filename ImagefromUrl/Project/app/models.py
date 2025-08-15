from django.db import models

# Create your models here.

class URLImage(models.Model):
    name = models.CharField(max_length=100)
    image_urls = models.JSONField(default=list)
    class Meta:
        db_table='URLImage'