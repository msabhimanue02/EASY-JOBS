# Generated by Django 4.1.5 on 2023-02-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='freelanceregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('resume', models.FileField(upload_to='documents/')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='providerregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('businesslicense', models.FileField(upload_to='documents/')),
                ('description', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='seekerregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact', models.IntegerField(max_length=10)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=30)),
                ('resume', models.FileField(upload_to='documents/')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
