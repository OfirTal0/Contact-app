# Generated by Django 4.2.7 on 2023-12-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='role',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
