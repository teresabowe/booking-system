# Generated by Django 3.2.16 on 2022-12-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deskbooking', '0003_alter_booking_desk'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('desk_booking_date', 'desk')},
        ),
    ]
