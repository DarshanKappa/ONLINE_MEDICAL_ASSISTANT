# Generated by Django 3.2 on 2021-05-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20210427_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_detail',
            name='d_comment_no',
            field=models.IntegerField(default='no comment'),
        ),
    ]
