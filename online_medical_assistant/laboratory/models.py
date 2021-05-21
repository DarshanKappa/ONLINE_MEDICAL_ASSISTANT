from django.db import models

# Create your models here.


class Laboratory(models.Model):

    id = models.IntegerField(primary_key=True)
    Lab_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    location = models.CharField(max_length=10000)
    lab_photo = models.ImageField(upload_to="lab_photo")
    certificate = models.ImageField(upload_to="lab_certificate")

class lab_type(models.Model):
    
    lab_id = models.IntegerField()
    test_type = models.CharField(max_length=50)


class Lab_appointment_list(models.Model):
    appointment_no = models.CharField(max_length=50)
    user_id = models.IntegerField()
    lab_id = models.IntegerField()
    doctor_appointment_no = models.IntegerField(null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    