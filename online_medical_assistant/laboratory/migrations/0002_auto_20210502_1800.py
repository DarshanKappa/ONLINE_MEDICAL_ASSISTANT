# Generated by Django 3.2 on 2021-05-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratory',
            name='certificate',
            field=models.ImageField(default=None, upload_to=None),
        ),
        migrations.AddField(
            model_name='laboratory',
            name='lab_photo',
            field=models.ImageField(default=None, upload_to=None),
        ),
    ]
