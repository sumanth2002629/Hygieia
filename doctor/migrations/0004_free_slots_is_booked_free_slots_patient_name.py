# Generated by Django 4.0.2 on 2022-06-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_free_slots_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_slots',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='free_slots',
            name='patient_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]