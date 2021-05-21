from django.shortcuts import render
from .models import District_city
from account.models import Profile
import os


# Create your views here.

def access():

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'district/.txt')
        

    f = open(file_path)

    data = []
    data1 = []
    data2 = []

    #part 1

    i = -1

    for j in f:
        data.append(j)
        i = i + 1



    for j in range(0,i):
        if j%2 == 0 or j == 0:
            data1.append(data[j])


    #part 2

    for i in data1:
        
        data2.append(i.replace('\n', ''))


    for i in data2:
        print(i)
        dc = District_city(district='',city=i)
        dc.save()
      




def data(request):
    
    # access()
    
    return render(request,'home.html')