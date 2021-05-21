from appointment.views import appointment
from typing import Tuple
from django.db import models

# Create your models here.


class new_Doctors_Appointment(models.Model):

    patient_id = models.IntegerField()
    name = models.CharField(max_length=50)
    appointment_no = models.CharField(primary_key=True,max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)
    Time = models.CharField(max_length=50,default='')
    address = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    blood = models.CharField(max_length=50)
    priscription_text = models.CharField(max_length=500,default='None')
    priscription_photo = models.ImageField(upload_to='priscription_photo', height_field=None, width_field=None, max_length=None,default='about.jpg')
    uploaded = models.CharField(max_length=50,default='no')


class doctor_appointment_list(models.Model):
    doctor_id = models.IntegerField()
    user_id = models.IntegerField()
    Date = models.DateField(auto_now=False, auto_now_add=False,default='2021-01-01')
    Time = models.CharField(max_length=50,default='')
    no_appointment = models.CharField(max_length=50,default='')


class Now_Appointment_No(models.Model):

    data_name = models.CharField(max_length=100)
    data = models.CharField(max_length=500)

    




