# Generated by Django 4.2.7 on 2023-12-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0004_remove_user_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='contact_app/static/contact_app/images'),
        ),
    ]
