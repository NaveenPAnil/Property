# Generated by Django 3.2.10 on 2023-09-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0009_remove_registrationdb_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistdb',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to='wishlist'),
        ),
    ]