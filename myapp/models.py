from django.db import models

# Create your models here.
class SalesData(models.Model):
    product = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product 
    
    @property 
    def revenue(self):
        return self.quantity * self.price 
    
