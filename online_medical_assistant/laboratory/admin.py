from django.contrib import admin
from .models import Laboratory, lab_type, Lab_appointment_list

# Register your models here.

admin.site.register(Laboratory)
admin.site.register(lab_type)
admin.site.register(Lab_appointment_list)