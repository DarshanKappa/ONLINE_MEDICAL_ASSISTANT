# Generated by Django 3.2 on 2021-05-19 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0018_delete_doctors_appointment'),
    ]

    operations = [

        migrations.AlterField(
            model_name='new_doctors_appointment',
            name='priscription_photo',
            field=models.ImageField(default='about.jpg', upload_to='priscription_photo'),
        ),
        migrations.AlterField(
            model_name='new_doctors_appointment',
            name='priscription_text',
            field=models.CharField(default='None', max_length=500),
        ),
    ]
