from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order,OrderDetails
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.user}{self.product}{self.quantity}"



class AddressDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    orderdetails=models.ForeignKey(OrderDetails,on_delete=models.CASCADE,related_name='orderdetails')
    #order=models.ManyToManyField(Order,related_name='order')
    Address=models.TextField()
    Phone_no=models.PositiveIntegerField()
    pin_code=models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.user)
    