# Generated by Django 4.0.1 on 2022-04-29 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_rename_phone_registration_mobile_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='mobile_number',
            new_name='mobilenumber',
        ),
    ]
