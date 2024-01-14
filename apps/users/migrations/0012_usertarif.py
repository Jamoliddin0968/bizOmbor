# Generated by Django 5.0 on 2024-01-14 15:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0001_initial'),
        ('users', '0011_delete_usertarif'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateField(auto_now_add=True)),
                ('tarif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tariff.tarif')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
