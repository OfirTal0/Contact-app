# Generated by Django 4.2.7 on 2023-12-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0007_remove_contact_user_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='none', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, default='none', max_length=20, null=True),
        ),
    ]
