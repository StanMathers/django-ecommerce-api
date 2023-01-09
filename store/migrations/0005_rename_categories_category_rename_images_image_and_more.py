# Generated by Django 4.1.5 on 2023-01-09 19:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0004_images"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Categories",
            new_name="Category",
        ),
        migrations.RenameModel(
            old_name="Images",
            new_name="Image",
        ),
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
        migrations.RenameModel(
            old_name="ProductsCategory",
            new_name="ProductCategory",
        ),
    ]