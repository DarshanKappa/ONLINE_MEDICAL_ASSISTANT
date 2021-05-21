from django.shortcuts import render, redirect
from account.models import Profile
from home.views import home
from account.views import login
from django.contrib import messages
from doctor.models import doctor_appointment_list, new_Doctors_Appointment
from laboratory.models import Laboratory, lab_type, Lab_appointment_list

# Create your views here.


def patient(request):
 
    current_user = request.user

    if current_user.is_authenticated:
        profile = Profile.objects.get(id=current_user.id)

        if profile.user == "doctor":

            doc_list = doctor_appointment_list.objects.all()
            doc_appoint = new_Doctors_Appointment.objects.all()

            list1 = [ ]
            uploaded = ""

            for i in doc_list:
                if current_user.id == i.doctor_id:
                    
                    list1.append(new_Doctors_Appointment.objects.get(appointment_no=i.no_appointment))


            


            return render(request,'patient.html',{'list1':list1})
        elif profile.user == 'laboratory':

            lab_list = Lab_appointment_list.objects.all()
            appointments = new_Doctors_Appointment.objects.all()

            list = [ ]

            for i in lab_list:
                if current_user.id == i.lab_id:
                    list.append(new_Doctors_Appointment.objects.get(appointment_no=i.appointment_no))
            
            return render(request,'lab_patient.html',{'list':list})

       

        else:
            return redirect('home')
    else:
        return redirect('login')



def search_appoint(request):

    current_user = request.user
    appoint_no = request.GET['appoint_no']

    list1 = [ ]
    for i in doctor_appointment_list.objects.all():
        if appoint_no == i.no_appointment and current_user.id == i.doctor_id:
            list1.append(new_Doctors_Appointment.objects.get(appointment_no=appoint_no))
            return render(request,'patient.html',{'list1':list1})



    messages.info(request,"Patient is not exist ")
    return redirect('patient')
    


def search_d_appoint(request):

    current_user = request.user
    date = request.GET['date']

    print(date)
    list1 = [ ]

    for i in doctor_appointment_list.objects.all():
        print(i.Date)
        if current_user.id == i.doctor_id:
            print("in")
            list1.append(new_Doctors_Appointment.objects.get(date=date))


    if list1 is not None:
        return render(request,'patient.html',{'list1':set(list1)})


    messages.info(request,"Patient is not exist ")
    return redirect('patient')



