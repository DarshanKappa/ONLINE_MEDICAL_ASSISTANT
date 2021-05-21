from django.db import models

# Create your models here.


class District_city(models.Model):
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)