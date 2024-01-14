# Generated by Django 5.0 on 2023-12-19 03:59

from django.db import migrations, models

import apps.products.models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.products.models._generate_filename),
        ),
    ]
