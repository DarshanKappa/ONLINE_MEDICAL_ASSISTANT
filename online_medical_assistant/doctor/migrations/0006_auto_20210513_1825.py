# Generated by Django 3.2 on 2021-05-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_auto_20210513_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_appointment_list',
            name='time',
        ),
        migrations.AddField(
            model_name='doctor_appointment_list',
            name='Time',
            field=models.CharField(default='', max_length=50),
        ),
    ]