# Generated by Django 5.0 on 2023-12-18 13:00

import apps.sales.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(default=apps.sales.models.get_current_date_as_integer)),
                ('discount', models.IntegerField()),
                ('cash', models.IntegerField()),
                ('without_cash', models.IntegerField()),
                ('total_summa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('amount', models.FloatField(default=0)),
                ('total', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_items', to='sales.sale')),
            ],
        ),
    ]
