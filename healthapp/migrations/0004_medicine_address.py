# Generated by Django 3.2 on 2021-05-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0003_appointment_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
