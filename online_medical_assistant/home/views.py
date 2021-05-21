from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.




def home(request):
    currnet_user = request.user

    return render(request,'home.html',{'data':'darahanp'})

