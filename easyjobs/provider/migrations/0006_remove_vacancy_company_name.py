# Generated by Django 4.1.5 on 2023-04-26 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_vacancy_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='company_name',
        ),
    ]
