# Generated by Django 3.2.10 on 2023-09-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0052_remove_paymentdb_bookingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selldb',
            name='Rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
