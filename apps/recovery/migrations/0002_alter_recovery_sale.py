# Generated by Django 5.0 on 2024-01-14 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('recovery', '0001_initial'),
        ('sales', '0003_sale_store_sale_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recovery',
            name='sale',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sale_recovery',
                                       to='sales.sale'),
        ),
    ]
