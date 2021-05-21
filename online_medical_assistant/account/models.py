from django.db import models

# Create your models here.


class Profile(models.Model):

    id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    languages = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50, default='blood group')
    gender = models.CharField(max_length=50, default='gender')
    Address = models.CharField(max_length=100, default='adress')
    district = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=10000, default='')
    photo = models.ImageField(upload_to='userphoto',default='')
    pin = models.CharField(max_length=50, default='')
    user = models.CharField(max_length=50,default='user')

    