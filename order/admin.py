from django.contrib import admin
from .models import Order,OrderDetails
# Register your models here.

class OrderDetailsInline(admin.TabularInline):
    model=OrderDetails
    extra=0
   # classes=['collapse']



class OrderAdmin(admin.ModelAdmin):
    list_display=['id','date_time','user','status']
    list_filter=['status']
    search_fields=['id','status']
    inlines=[OrderDetailsInline]


admin.site.register(Order,OrderAdmin)




