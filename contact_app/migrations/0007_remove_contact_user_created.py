# Generated by Django 4.2.7 on 2023-12-16 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0006_contact_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_created',
        ),
    ]
