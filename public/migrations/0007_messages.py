# Generated by Django 4.0.1 on 2022-04-30 09:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_alter_registration_working_department'),
        ('public', '0006_complaints_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('messages_text', models.TextField(default='null')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('complaints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.complaints')),
                ('department_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.registration')),
                ('public_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.registration')),
            ],
        ),
    ]
