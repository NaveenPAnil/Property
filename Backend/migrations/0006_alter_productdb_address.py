# Generated by Django 3.2.10 on 2023-09-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_membersdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='Address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
