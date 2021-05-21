# Generated by Django 3.2 on 2021-05-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_auto_20210515_1800'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='doctor_appointment_list',
            name='priscription_photo',
        ),
        migrations.RemoveField(
            model_name='doctor_appointment_list',
            name='priscription_text',
        ),
        migrations.RemoveField(
            model_name='doctor_appointment_list',
            name='uploaded',
        ),
        migrations.AddField(
            model_name='new_doctors_appointment',
            name='priscription_photo',
            field=models.ImageField(default='', upload_to='priscription_photo'),
        ),
        migrations.AddField(
            model_name='new_doctors_appointment',
            name='priscription_text',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='new_doctors_appointment',
            name='uploaded',
            field=models.CharField(default='no', max_length=50),
        ),
    ]