# Generated by Django 3.2 on 2021-05-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0006_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='Amount_to_be_paid',
            field=models.IntegerField(default=500),
        ),
    ]
