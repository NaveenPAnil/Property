# Generated by Django 3.2.10 on 2023-08-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Property_place', models.CharField(blank=True, max_length=100, null=True)),
                ('Property_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Bedroom', models.IntegerField(blank=True, null=True)),
                ('Bathroom', models.IntegerField(blank=True, null=True)),
                ('Property_Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Rate', models.CharField(blank=True, max_length=50, null=True)),
                ('SqFeet', models.CharField(blank=True, max_length=50, null=True)),
                ('Photo1', models.ImageField(blank=True, null=True, upload_to='sellproperties')),
                ('Photo2', models.ImageField(blank=True, null=True, upload_to='sellproperties')),
                ('Photo3', models.ImageField(blank=True, null=True, upload_to='sellproperties')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('User_Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Profile_Picture', models.ImageField(blank=True, null=True, upload_to='user_image')),
            ],
        ),
    ]
