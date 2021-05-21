# Generated by Django 3.2 on 2021-05-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_auto_20210515_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_Doctors_Appointment',
            fields=[
                ('pk_id', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('appointment_no', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('Time', models.CharField(default='', max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('blood', models.CharField(max_length=50)),
            ],
        ),

    ]

