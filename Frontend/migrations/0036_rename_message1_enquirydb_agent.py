# Generated by Django 3.2.10 on 2023-09-10 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0035_enquirydb_message1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquirydb',
            old_name='Message1',
            new_name='Agent',
        ),
    ]
