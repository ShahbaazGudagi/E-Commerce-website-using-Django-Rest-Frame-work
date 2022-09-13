from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class ProductCategory(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
class Product(models.Model):
    product_category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name="Product")
    name=models.CharField(max_length=150)
    slug=models.SlugField()
    price=models.FloatField(validators=[MinValueValidator(0)])
    cover_image=models.ImageField()
    status=models.BooleanField(default=True)
    description=models.TextField()
    

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductImage")
    image=models.ImageField()

    def __str__(self):
        return str(self.product)
    
