# Generated by Django 3.2.10 on 2023-09-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0018_remove_wishlistdb_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
