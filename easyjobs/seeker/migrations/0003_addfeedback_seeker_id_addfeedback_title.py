# Generated by Django 4.1.5 on 2023-03-27 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobadmin', '0005_freelanceregistration_status'),
        ('seeker', '0002_addfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='addfeedback',
            name='seeker_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobadmin.seekerregistration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addfeedback',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
