# Generated by Django 3.1.1 on 2020-10-23 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0018_auto_20201023_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdetail',
            name='newsHead',
        ),
        migrations.RemoveField(
            model_name='newsdetail',
            name='newsImg',
        ),
    ]
