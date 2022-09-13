from django.contrib import admin
from .models import *
# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['name','status']
    search_fields=['name']
    list_filter=['status']

admin.site.register(ProductCategory,ProductCategoryAdmin)


class ProductImagesInlines(admin.TabularInline):
    model=ProductImage
    extra=0

    
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','product_category','price','status']
    search_fields=['name','price']
    list_filter=['status','product_category']
    inlines= [ProductImagesInlines]


admin.site.register(Product,ProductAdmin)

