# Generated by Django 3.1.1 on 2020-10-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0014_auto_20201022_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcometab4',
            name='displayName2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='welcometab4',
            name='file1',
            field=models.FileField(max_length=50, upload_to='welcFiles'),
        ),
        migrations.AlterField(
            model_name='welcometab4',
            name='file2',
            field=models.FileField(blank=True, max_length=50, null=True, upload_to='welcFiles'),
        ),
    ]
