from django.contrib import admin
from .models import Categories, Products, ProductsCategory, Images

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(Images)

