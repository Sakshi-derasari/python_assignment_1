from django.db import models
from decimal import Decimal

# Create your models here. 

class Add_to_cart(models.Model):
    product_name = models.CharField(max_length=40)
    product_discription = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    qty = models.IntegerField(null=True)
    img = models.ImageField(upload_to="images",null=True)
    product_discount = models.DecimalField(max_digits=5,decimal_places=2,help_text="Discount percentage (e.g. 10 for 10%)")
    @property
    def totale_price(self):
        discount_amount = (self.product_discount / Decimal(100)) * self.product_price
        return discount_amount * self.qty
    
    def __str__(self):
        return self.product_name 



