# Generated by Django 3.2.10 on 2023-09-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0061_alter_paymentdb_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdb',
            name='Expiry_date',
            field=models.CharField(help_text='Format: MM/YY', max_length=5, null=True),
        ),
    ]