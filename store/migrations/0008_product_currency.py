# Generated by Django 4.1.5 on 2023-01-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_rename_uploaded_product_added"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="currency",
            field=models.CharField(default="GEL", max_length=3),
        ),
    ]
