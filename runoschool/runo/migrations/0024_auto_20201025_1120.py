# Generated by Django 3.1.1 on 2020-10-25 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0023_steps'),
    ]

    operations = [
        migrations.RenameField(
            model_name='steps',
            old_name='desc',
            new_name='step',
        ),
    ]
