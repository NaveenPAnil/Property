# Generated by Django 3.2.10 on 2023-08-18 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_productdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='Category2_Name',
        ),
    ]