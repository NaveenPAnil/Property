# Generated by Django 3.2.10 on 2023-09-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0013_alter_registrationdb_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Mail', models.EmailField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Property_Address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='wishlistdb',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to='wishlist'),
        ),
        migrations.AlterField(
            model_name='registrationdb',
            name='Username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
