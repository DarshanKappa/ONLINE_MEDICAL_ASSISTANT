from django.contrib import admin
from .models import doctor_appointment_list,Now_Appointment_No,new_Doctors_Appointment

# Register your models here.

admin.site.register(doctor_appointment_list)
admin.site.register(Now_Appointment_No)
admin.site.register(new_Doctors_Appointment)