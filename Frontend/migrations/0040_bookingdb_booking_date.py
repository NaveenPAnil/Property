# Generated by Django 3.2.10 on 2023-09-12 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0039_bookingdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='Booking_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
