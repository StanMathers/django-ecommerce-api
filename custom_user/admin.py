from django.contrib import admin
from .models import Customer, UserStatus

# Register your models here.
admin.site.register(Customer)
admin.site.register(UserStatus)
