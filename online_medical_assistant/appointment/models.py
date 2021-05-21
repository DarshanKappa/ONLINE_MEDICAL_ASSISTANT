from django.db import models

# Create your models here.

class Doctor:
    id: int
    name: str


class Doctor_Detail(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    primary_location = models.CharField(max_length=100)
    type_doctor = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)
    surgeon = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    d_rating = models.FloatField(default=4.5)
    d_patient_satis_rating = models.IntegerField(default=0)
    d_comment_no = models.IntegerField(default='0')
    doc_phone = models.CharField(max_length=10,default=' ')
    doc_phone2 = models.CharField(max_length=10,default=' ')
    doc_email = models.EmailField(max_length=254,default=' ')
    certificate1 = models.ImageField(upload_to='doctor_certificates',default=' ')
    certificate2 = models.ImageField(upload_to='doctor_certificates',default=' ')
    certificate3 = models.ImageField(upload_to='doctor_certificates',default=' ')
    photo1 = models.ImageField(upload_to='doctor_photo',default=' ')
    photo2 = models.ImageField(upload_to='doctor_photo',default=' ')
    




