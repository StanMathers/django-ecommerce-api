from django.db import models
from ecommerce_api.settings import AUTH_USER_MODEL

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit_price = models.PositiveBigIntegerField()
    discount = models.PositiveBigIntegerField(blank=True, null=True)
    stock = models.PositiveBigIntegerField(blank=True, null=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1)
    
    def __str__(self):
        return self.name
    

class ProductsCategory(models.Model):
    # Assosiation table
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product.name} - {self.category.name}'

