# Generated by Django 3.2.10 on 2023-09-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0011_remove_wishlistdb_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdb',
            name='Username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]