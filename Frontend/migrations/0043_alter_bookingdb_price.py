# Generated by Django 3.2.10 on 2023-09-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0042_auto_20230912_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdb',
            name='Price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
