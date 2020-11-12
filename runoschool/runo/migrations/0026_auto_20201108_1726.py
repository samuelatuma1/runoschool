# Generated by Django 3.1.1 on 2020-11-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0025_admitfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=30)),
                ('access_key', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classRoom', models.CharField(choices=[('Nursery1', 'Nursery1'), ('Nursery2', 'Nursery2')], max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('classMail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('teacher', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Nursery1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(blank=True, max_length=150)),
                ('note', models.CharField(blank=True, max_length=150)),
                ('DOB', models.DateField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('classRoom', models.CharField(choices=[('Nursery1', 'Nursery1')], default='Nursery1', max_length=15)),
                ('Term1', models.FileField(blank=True, upload_to='term1')),
                ('Term2', models.FileField(blank=True, upload_to='term2')),
                ('Term3', models.FileField(blank=True, upload_to='term3')),
                ('remark', models.CharField(choices=[('promote', 'promote'), ('repeat', 'repeat'), ('noChange', 'noChange')], default='noChange', max_length=15)),
                ('status', models.CharField(choices=[('active', 'active'), ('dormant', 'dormant')], default='active', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Nursery2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(blank=True, max_length=150)),
                ('note', models.CharField(blank=True, max_length=150)),
                ('classRoom', models.CharField(choices=[('Nursery2', 'Nursery2')], default='Nursery2', max_length=15)),
                ('Term1', models.FileField(blank=True, upload_to='term1')),
                ('Term2', models.FileField(blank=True, upload_to='term2')),
                ('Term3', models.FileField(blank=True, upload_to='term3')),
                ('DOB', models.DateField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('remark', models.CharField(choices=[('promote', 'promote'), ('repeat', 'repeat'), ('noChange', 'noChange')], default='noChange', max_length=15)),
                ('status', models.CharField(choices=[('active', 'active'), ('dormant', 'dormant')], default='active', max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='admitfiles',
            name='file1',
            field=models.FileField(null=True, upload_to='admission_files'),
        ),
        migrations.AlterField(
            model_name='admitfiles',
            name='name1',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='admitfiles',
            name='name2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='admitfiles',
            name='name3',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
