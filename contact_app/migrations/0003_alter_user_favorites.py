# Generated by Django 4.2.7 on 2023-12-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_contact_description_alter_contact_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.CharField(max_length=200),
        ),
    ]
