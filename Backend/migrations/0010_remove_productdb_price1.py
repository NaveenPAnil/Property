# Generated by Django 3.2.10 on 2023-09-12 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_productdb_price1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='Price1',
        ),
    ]
