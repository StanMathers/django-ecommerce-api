# Generated by Django 4.1.5 on 2023-01-10 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_rename_categories_category_rename_images_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="uploaded",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
