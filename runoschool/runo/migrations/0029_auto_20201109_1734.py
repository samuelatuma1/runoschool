# Generated by Django 3.1.1 on 2020-11-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0028_footerabout_footerdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerabout',
            name='school_about',
            field=models.TextField(max_length=600),
        ),
    ]
