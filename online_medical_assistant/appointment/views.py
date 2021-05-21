from account.models import Profile
from django.shortcuts import render, redirect
from .models import Doctor, Doctor_Detail
from django.contrib.auth import authenticate, login, logout
from home.views import home
from account.views import login
from data.models import District_city


# Create your views here.

# def appointment(request):

#     dest1 = Doctor()

#     dest1.name = "Darshan Prajapati"
#     dest2 = Doctor()

#     dest2.name = "Sahil Chauhan"
#     dest3 = Doctor()

#     dest3.name = "Jaimin Jethava"
#     dest4 = Doctor()

#     dest4.name = "Chirag Thakkar"
#     dest5 = Doctor()

#     dest5.name = "Satyam Pandya"

#     dests = [dest1,dest2,dest3,dest4,dest5]

#     return render(request,'appointment.html',{'dests':dests})



def appointment(request):

    if request.user.is_authenticated:
        current_user = request.user
      
        list1 = [ ]
        dc = District_city.objects.all()
        
        for i in dc:
            list1.append(i.district)
     

        doctord = Doctor_Detail.objects.all()
        
        return render(request,'appointment.html',{'doctord':doctord,'dist_citys':sorted(list(set(list1)))})
    else:
        return redirect('login')


def doctors_type(request):

    doctors_type = request.POST.get('doctors_type','')
    print(doctors_type)
    
    list_of_district = [ ]
    list_of_doctors = [ ]

    doctors = Doctor_Detail.objects.all()

    for i in doctors:
        if doctors_type == i.type_doctor:
            list_of_district.append(i.district)
            list_of_doctors.append(i)

    return render(request,'appointment.html',{  'doctord':list_of_doctors,
                                                'list_of_district':sorted(list(set(list_of_district))),
                                                'doc_fild':doctors_type
                                                })



def district(request):
    doctors_type = request.POST.get('doctors_type','')
    print(doctors_type)
    district = request.POST.get('district','')
    print(district)

    list_of_doctors = [ ]
    list_of_district = [ ]
    list_of_city = [ ]

    doctors = Doctor_Detail.objects.all()

    for i in doctors:
        if doctors_type == i.type_doctor:
            list_of_district.append(i.district)
            if district == i.district:
                list_of_city.append(i.city)
                list_of_doctors.append(i)

    return render(request,'appointment.html',{
                                                'doctord':list_of_doctors,
                                                'list_of_district':sorted(list(set(list_of_district))),
                                                'list_of_city':sorted(list(set(list_of_city))),
                                                'doc_fild':doctors_type,
                                                'dist_fild':district

                                            })




def city(request):
    
    doc_type = request.POST.get('doctors_type','')
    district = request.POST.get('district','')
    city = request.POST.get('city','')
    print(doc_type)
    print(district)
    print(city)

    list_of_doctors = [ ]
    list_of_district = [ ]
    list_of_city = [ ]

    doctors = Doctor_Detail.objects.all()

    for i in doctors:
        if doc_type == i.type_doctor:
            list_of_district.append(i.district)
            if district == i.district:
                list_of_city.append(i.city)
                if city == i.city:
                    list_of_doctors.append(i)

    return render(request,'appointment.html',{
                                                'doctord':list_of_doctors,
                                                'list_of_district':sorted(list(set(list_of_district))),
                                                'list_of_city':sorted(list(set(list_of_city))),
                                                'doc_fild':doc_type,
                                                'dist_fild':district
                                              })
