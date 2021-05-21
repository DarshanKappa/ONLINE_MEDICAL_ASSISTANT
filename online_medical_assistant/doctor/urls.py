from django.urls import path
from . import views

urlpatterns = [
    path("",views.doctor,name="doctor"),
    path("test/",views.test,name="test"),
    path("docdata/",views.docdata,name="docdata"),
    path("doctakeappoint/",views.doctakeappoint,name="doctakeappoint"),
    path("upload_priscription/",views.upload_priscription,name="upload_priscription"),
]