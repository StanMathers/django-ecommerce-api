# Generated by Django 4.1.5 on 2023-01-10 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_product_uploaded"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="uploaded",
            new_name="added",
        ),
    ]
