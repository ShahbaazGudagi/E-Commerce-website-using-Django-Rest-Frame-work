from dataclasses import field, fields
from email.headerregistry import Address
from functools import partial
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from order.models import Order,OrderDetails
from product.models import ProductCategory,Product,ProductImage
from django.contrib.auth.models import User
from cart.models import Cart,AddressDetails

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields='__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    ProductImage=ProductImageSerializer(many=True)
    class Meta:
        model=Product
        fields='__all__'
        



class CustomerSerializer(serializers.ModelSerializer):   
    class Meta:
        model=User
        fields=[
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
            ]
        extra_kwargs={
            'password':{
                'write_only' : True
            }
        }
    def create(self,validatedData):
        user=User.objects.create(
            username=validatedData['username'],
            first_name=validatedData['first_name'],
            last_name=validatedData['last_name'],
            email=validatedData['email'],
        )   
        user.set_password(validatedData['password']) 
        user.save()
        return user
    
    def update(self,userObject,validatedData):
        if validatedData.get('password'):
            userObject.set_password(validatedData.get('password'))
        userObject.save()
        return validatedData
    


class CartSerializer(serializers.ModelSerializer):
  #  Product=ProductSerializer(many=True)
    class Meta:
        model=Cart
        fields=['id','product','quantity']

class CheckoutSerializer(serializers.Serializer):
    payment_id=serializers.CharField(max_length=30)
    transaction_id=serializers.CharField(max_length=50)



class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails
        fields='__all__'

#------------------------------------------------------------------------------------------------



class OrderSerializer(serializers.ModelSerializer):
    OrderDetails=OrderDetailsSerializer(many=True)
    class Meta:
        model=Order
        fields='__all__'


class AddressDetailSerializer(serializers.ModelSerializer):
    orderdetails=OrderDetailsSerializer(partial=True)
    class Meta:
        model=AddressDetails
        fields='__all__'

#------------------------------------------------------------------