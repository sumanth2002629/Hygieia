# Generated by Django 4.0.2 on 2022-06-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_free_slots_is_booked_free_slots_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_slots',
            name='time',
            field=models.DateTimeField(),
        ),
    ]