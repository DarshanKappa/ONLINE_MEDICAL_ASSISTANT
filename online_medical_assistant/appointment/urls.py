from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointment,name='appointment'),
    path('doctors_type',views.doctors_type,name='doctors_type'),
    path('district',views.district,name='district'),
    path('city',views.city,name='city'),
]