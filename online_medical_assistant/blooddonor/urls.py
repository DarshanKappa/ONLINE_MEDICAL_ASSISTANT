from django.urls import path
from . import views

urlpatterns = [
    path("",views.blood_donor,name="blood_donor"),
    path("search_blood_group",views.search_bg,name="search_bg"),
    path("search_district_bg",views.search_district_bg,name="search_district_bg"),
    path("search_city_bg",views.search_city_bg,name="search_city_bg"),
]