from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="UserProfile")
    address=models.TextField(null=True,blank=True)
    mobile=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.user)
        