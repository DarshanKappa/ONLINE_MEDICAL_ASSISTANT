# Generated by Django 3.2 on 2021-05-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20210513_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_appointment_list',
            name='date',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
