# Generated by Django 4.0.3 on 2022-03-24 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0008_alter_pay_amount_to_be_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='Postal Code',
            new_name='Postalcode',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='Postal Code',
        ),
    ]
