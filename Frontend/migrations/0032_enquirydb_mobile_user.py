# Generated by Django 3.2.10 on 2023-09-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0031_auto_20230909_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirydb',
            name='Mobile_User',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
