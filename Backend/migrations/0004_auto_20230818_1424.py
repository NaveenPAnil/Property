# Generated by Django 3.2.10 on 2023-08-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_remove_productdb_category2_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='Agent_Address',
        ),
        migrations.AddField(
            model_name='productdb',
            name='Agent_Place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
