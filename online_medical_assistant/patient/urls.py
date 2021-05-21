from django.urls import path
from . import views

urlpatterns = [
    path("",views.patient,name="patient"),
    path("search_appointment",views.search_appoint,name="search_appoint"),
    path("search_date_appointment",views.search_d_appoint,name="search_d_appoint"),
]

