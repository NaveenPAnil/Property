# Generated by Django 3.2.10 on 2023-09-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0034_remove_enquirydb_agent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirydb',
            name='Message1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
