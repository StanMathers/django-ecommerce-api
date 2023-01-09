from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.PositiveBigIntegerField()
    discount = models.PositiveBigIntegerField(blank=True, null=True)
    stock = models.PositiveBigIntegerField(blank=True, null=True)
    

class ProductsCategory(models.Model):
    # Assosiation table
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

