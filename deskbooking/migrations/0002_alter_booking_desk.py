# Generated by Django 3.2.16 on 2022-11-29 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deskbooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='desk',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='desk_booking', to='deskbooking.desk'),
        ),
    ]
