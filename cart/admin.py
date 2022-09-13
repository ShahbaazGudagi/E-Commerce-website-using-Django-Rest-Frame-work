from django.contrib import admin
from .models import AddressDetails, Cart
# Register your models here.

admin.site.register(Cart)

#--------------------------------------------------------------------

class AdminAddressDetails(admin.ModelAdmin):
    list_display=['user','Address','Phone_no','pin_code']


admin.site.register(AddressDetails,AdminAddressDetails)