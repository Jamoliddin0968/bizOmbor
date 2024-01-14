# Generated by Django 5.0 on 2024-01-14 13:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import apps.tools.utils


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('products', '0003_product_store'),
        ('sales', '0003_sale_store_sale_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=apps.tools.utils.get_current_date_as_integer)),
                ('total_summa', models.IntegerField(default=0)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_recovery',
                                           to='sales.sale')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('recovery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items',
                                               to='recovery.recovery')),
            ],
        ),
    ]
