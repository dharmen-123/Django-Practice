from django.db import models

# Create your models here.

class ItemInfo(models.Model):
    itemname=models.CharField(max_length=100)
    itemdes=models.CharField()
    itemprice=models.IntegerField()
    itemimage=models.ImageField(upload_to='file')
    itemcolor=models.CharField()
    
class Payment(models.Model):
    order_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()  # Stored in paise
    status = models.CharField(max_length=20, default="Created")  # Created, Paid, Failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - ₹{self.amount / 100:.2f}"


