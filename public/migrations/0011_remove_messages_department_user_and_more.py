# Generated by Django 4.0.1 on 2022-04-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_remove_messages_public_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='department_user',
        ),
        migrations.AddField(
            model_name='messages',
            name='department_user_id',
            field=models.IntegerField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='messages',
            name='public_user_id',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]