# Generated by Django 3.2.10 on 2023-09-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0008_alter_productdb_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Price1',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
