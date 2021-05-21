from appointment.views import appointment
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from appointment.models import Doctor_Detail
from account.models import Profile
from .models import doctor_appointment_list
from .models import new_Doctors_Appointment
from home.views import home
from datetime import datetime, time, timedelta, date
from .models import Now_Appointment_No
from patient.views import patient
from data.models import District_city

# Create your views here.

def test(request):
    print("...........start..........")
 
    data = District_city.objects.all()
    list = [ ]
    for i in data:
        if i.district == "Ahmedabad":
            list.append(i.city)

    for i in sorted(list):
        print(i)


    # x = datetime.now() - timedelta(days=1) + timedelta(days=2)
    # x1 = datetime(2021,5,17).weekday()
    
    # print(x1)
   
    # print(x.date())
    # d = datetime.now() - timedelta(days=1)
    # for i in range(0,10):
    #     if d.weekday() == 6:
    #         d = d + timedelta(days=2)
    #     else:
    #         d = d + timedelta(days=1)

    # print(d.date())




    # no = Now_Appointment_No.objects.get(data_name="current_appointment_no")
    # no.data = str(int(no.data) + 1)
 
    # print(no.data)
    return redirect('home')

def docdata(request):


    data = request.POST['data']
    print(data)

    doctord = Doctor_Detail.objects.all()

    return render(request,'appointment.html',{'doctord':doctord,'block1':'block','doctorname':data})


def doctakeappoint(request):

    current_user = request.user

    date = request.POST['date']
    time = request.POST['times']
    id = request.POST['id']
    print(date)

    user = User.objects.get(id=current_user.id)
    profile = Profile.objects.get(id=current_user.id)
    no = Now_Appointment_No.objects.get(data_name="current_appointment_no")
    no.data = str(int(no.data) + 1)
    print(no.data)
    x = datetime.now() - timedelta(days=1)
    for i in range(0,int(date)):
        if x.weekday() == 5:
            x = x + timedelta(days=2)
        else:
            x = x + timedelta(days=1)
    print(x)


    doc_appoint_det = new_Doctors_Appointment(patient_id=user.id,name=user.first_name+" "+user.last_name,dob=profile.date_of_birth,phone=user.username,email=user.email,date=x,Time=time,address=profile.Address,zip_code=profile.pin,language=profile.languages,blood=profile.blood_group,appointment_no=no.data)
    doc_appoint_det.save()

    appoint_list = doctor_appointment_list(doctor_id=id,user_id=user.id,Date=x,Time=time,no_appointment=no.data)
    appoint_list.save()

    no.save()



    return redirect('home')




def doctor(request):

    if request.method == 'POST':
        print('in')

        profile = Profile.objects.all()
        cu = request.user
        for i in profile:
            if cu.id == i.id:
                profile = i

        id = cu.id
        name = cu.first_name+" "+cu.last_name
        degree = request.POST['degree']
        department = request.POST['department']
        primary_location = request.POST['primary_location']
        type_doctor = request.POST['type_doctor']
        language = profile.languages
        # surgeon = request.POST['surgeon123']
        # if surgeon == "on":
        #     surgeon = True
        # else:
        #     surgeon = False
        address = request.POST['address']
        city = profile.city
        district = profile.district
        phone1 = cu.username
        phone2 = request.POST['phone']
        email = cu.email
        certificat1 = request.FILES['certificates1']
        certificat2 = request.FILES['certificates2']
        certificat3 = request.FILES['certificates3']
        photo1 = request.FILES['photos1']
        photo2 = request.FILES['photos2']

        doctor = Doctor_Detail(id=id,name=name,degree=degree,department=department,primary_location=primary_location,type_doctor=type_doctor,languages=language,address=address,city=city,district=district,doc_phone=phone1,doc_phone2=phone2,doc_email=email,certificate1=certificat1,certificate2=certificat2,certificate3=certificat3,photo1=photo1,photo2=photo2)
        
        doctor.save()

        doc = Profile.objects.get(id=cu.id)
        doc.user = 'doctor'
        doc.save()
        
     
        return redirect('home')

     

    else:
        print('out')
        return render(request,'doctor_register.html')


def upload_priscription(request):
    
    photo = request.FILES['photo']
    text = request.POST['text']
    appointment = request.POST['id']

    patient = new_Doctors_Appointment.objects.get(appointment_no=appointment)
    patient.priscription_photo = photo
    patient.priscription_text = text
    patient.uploaded = "Uploaded"
    patient.save()

    return redirect('patient')


