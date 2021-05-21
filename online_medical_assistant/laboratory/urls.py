from django.urls import path
from . import views

urlpatterns = [
    path("",views.laboratory,name="laboratory"),
    path("lab_register",views.lab_register,name="lab_register"),
    path("show/",views.show,name="show"),
    path("search_lab/",views.search_lab,name="search_lab"),
    path("search_district_lab/",views.search_district_lab,name="search_district_lab"),
    path("search_city_lab/",views.search_city_lab,name="search_city_lab"),
    path("dtoclab/",views.dtoclab,name="dtoclab"),
    path("labiddata/",views.labiddata,name="labiddata"),
    path("labtakeappointment/",views.labtakeappoint,name="labtakeappoint"),

]
  