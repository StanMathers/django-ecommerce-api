import datetime
from django.db import models
from ecommerce_api.settings import AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    CURRENCY_CHOICES = [("USD", "USD"), ("GEL", "GEL"), ("EUR", "EUR")]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit_price = models.PositiveBigIntegerField()
    currency = models.CharField(max_length=3, default="GEL", choices=CURRENCY_CHOICES)
    discount = models.PositiveBigIntegerField(blank=True, null=True)
    stock = models.PositiveBigIntegerField(blank=True, null=True)
    added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    # Assosiation table
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.category.name}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media_root/")
