# Generated by Django 3.2.10 on 2023-09-08 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0025_rename_mobile_selldb_mobile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selldb',
            old_name='Mobile_User',
            new_name='Mobile',
        ),
    ]