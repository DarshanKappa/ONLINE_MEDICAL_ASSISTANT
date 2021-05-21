from appointment.views import appointment
from django.shortcuts import render,redirect
from account.models import Profile
from django.contrib.auth.models import User
from doctor.models import doctor_appointment_list, new_Doctors_Appointment
from appointment.models import Doctor_Detail
from datetime import date, datetime, timedelta
from laboratory.models import Lab_appointment_list, Laboratory, lab_type

# Create your views here.
 

def profile(request):

    #details
    curren_user = request.user
    profile = Profile.objects.all()
    profile1 = 0
    for i in profile:
        if curren_user.id == i.id:
            profile1 = i
            print(i.id)


    #appointments
    cu = request.user

    list = [ ]
    list2 = [ ]
    list3 = [ ]
    new_list = [ ]
    newappointlist = [ ]
    old_list = [ ]
    doc_list = [ ]
    appoint = new_Doctors_Appointment.objects.all()
    a_list = doctor_appointment_list.objects.all()
    doc_det = Doctor_Detail.objects.all()   


    for i in a_list:
        if cu.id == i.user_id:
            list.append(i)
            doc_list.append(Doctor_Detail.objects.get(id=i.doctor_id))
            for j in range(1,13):
                if i.Date == (datetime.now()+timedelta(days=j)).date():
                    list2.append(new_Doctors_Appointment.objects.get(appointment_no=i.no_appointment))
            if i.Date <= (datetime.now()).date():
                list3.append(new_Doctors_Appointment.objects.get(appointment_no=i.no_appointment))
    
    #lab appointments
    l_list1 = [ ]
    newl_list = [ ]
    oldl_list = [ ]
    profilel = [ ]
    laboratory_list = Laboratory.objects.all()
    lab_types = lab_type.objects.all()
    l_list = Lab_appointment_list.objects.all()


    for i in l_list:
        if cu.id == i.user_id:
            profilel.append(User.objects.get(id=i.lab_id))
            l_list1.append(i)
            for j in range(1,12):
                if i.date == (datetime.now()+timedelta(days=j)).date():
                    newl_list.append(new_Doctors_Appointment.objects.get(appointment_no=i.appointment_no))
            if i.date <= (datetime.now()).date():
                oldl_list.append(new_Doctors_Appointment.objects.get(appointment_no=i.appointment_no))
 

 
    return render(request,'myprofile.html',{'userdata':curren_user,
                                            'userprofile':profile1,

                                            'list':list,
                                            'appoint_list':list2,
                                            'doc_list':set(doc_list),
                                            'old_appoint_list':list3,

                                            'lab_list':set(l_list1),
                                            'lab_appointments':set(newl_list),
                                            'laboratorys':set(laboratory_list),
                                            'lab_type':set(lab_types),
                                            'lab_profile':set(profilel)
                                            })
 



def upload(request):
    photo = request.FILES['uploaddata']
    print("......photo has uploaded........")

    current_user = request.user
    profile2 = Profile.objects.get(id=current_user.id)

    profile2.photo = photo
    profile2.save()
    print(profile2.Address)


    return redirect('profile')

# def patient_appointment(request):
#     cu = request.user

#     main_list = [ ]
#     doc_list = [ ]
#     a_list = doctor_appointment_list.objects.all()
#     doc_det = Doctor_Detail.objects.all()   

#     for i in a_list:
#         if cu.id == i.user_id:
#             main_list.append(i)

#     for i in main_list:
#         for j in doc_det:
#             if i.doctor_id == j.id:
#                 doc_list.append(j)

#     return render(request,'myprofile.html',{'appoint_details':set(doc_list),'main_list':main_list})
        







