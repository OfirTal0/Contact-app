# Generated by Django 4.2.7 on 2023-12-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(max_length=20),
        ),
    ]