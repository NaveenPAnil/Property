# Generated by Django 3.2.10 on 2023-09-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0019_enquirydb'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistdb',
            name='Category_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
