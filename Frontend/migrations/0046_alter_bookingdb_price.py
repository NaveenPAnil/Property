# Generated by Django 3.2.10 on 2023-09-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0045_alter_bookingdb_bookingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdb',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
