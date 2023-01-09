from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserStatus(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Customer(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    billing_address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    user_status = models.ForeignKey(UserStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

