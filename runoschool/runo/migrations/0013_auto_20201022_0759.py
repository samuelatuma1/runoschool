# Generated by Django 3.1.1 on 2020-10-22 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0012_auto_20201021_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Welcometab3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resources', models.CharField(blank=True, max_length=150, null=True)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact1', models.CharField(max_length=100)),
                ('contact2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Welcometab4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(max_length=30, upload_to='welcFiles')),
                ('file2', models.FileField(blank=True, max_length=30, null=True, upload_to='welcFiles')),
            ],
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='contact1',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='contact2',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='email1',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='file1',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='file2',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='resources',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='write2',
        ),
        migrations.RemoveField(
            model_name='welcometab',
            name='writeHead2',
        ),
        migrations.AlterField(
            model_name='welcometab',
            name='writeHead1',
            field=models.CharField(default='This is testing', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Welcometab2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writeHead2', models.CharField(max_length=100)),
                ('write2', models.TextField(blank=True, null=True)),
                ('img2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='welcHome2', to='runo.welcimgs')),
            ],
        ),
    ]
