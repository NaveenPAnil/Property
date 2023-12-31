# Generated by Django 3.2.10 on 2023-08-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Category2_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Propertyplace', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Bedrooms', models.IntegerField(blank=True, null=True)),
                ('Bathrooms', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Price', models.CharField(blank=True, max_length=50, null=True)),
                ('Sqfeet', models.CharField(blank=True, max_length=50, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='properties')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='properties')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='properties')),
                ('Agent_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Designation', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Agent_Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Profile', models.ImageField(blank=True, null=True, upload_to='agent')),
            ],
        ),
    ]
