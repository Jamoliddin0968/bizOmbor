# Generated by Django 5.0 on 2024-06-22 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_store_alter_product_id'),
        ('versions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='versions.version'),
        ),
    ]
