# Generated by Django 4.0.1 on 2022-04-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='status',
            field=models.CharField(choices=[('send', 'Send'), ('reply', 'Reply')], default='send', max_length=15),
        ),
    ]
