# Generated by Django 4.0.1 on 2022-04-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0011_remove_messages_department_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='department_user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='messages',
            name='public_user_id',
            field=models.IntegerField(default=0),
        ),
    ]