from django.shortcuts import render, redirect
from .models import Laboratory,lab_type
from home.views import home
from django.contrib import messages
from data.models import District_city
from account.models import Profile
from .models import Lab_appointment_list
from doctor.models import Now_Appointment_No, new_Doctors_Appointment
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your views here.

def laboratory(request):

    lab = Laboratory.objects.all()

    
    test = lab_type.objects.all()
    district = [ ]
    city = [ ]
    tests = [ ]
    
    for l in lab:
        district.append(l.district)

    for i in lab:
        city.append(i.city)

    for j in test:
        tests.append(j.test_type)



    return render(request,'laboratory.html',{'lab':lab,'test':test,'dist':set(district),'city':set(city),'tests':set(tests)})

def data():

    lab = Laboratory.objects.all()

    
    test = lab_type.objects.all()
    district = [ ]
    city = [ ]
    tests = [ ]
    
    for l in lab:
        district.append(l.district)

    for i in lab:
        city.append(i.city)

    for j in test:
        tests.append(j.test_type)

    return tests,district,city

def dtoclab(request):
    if request.method == "POST":

        current_user = request.user

        lab_name = request.POST['lab']
        type_of_test = request.POST['tot']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        district = request.POST['dist']
        photo = request.POST['photo']
        certificate = request.POST['certificate']

        if len(str(city)) < 1:
            messages.info(request,"please select a city")
            data = [lab_name,type_of_test,email,phone,address,district,photo,certificate]
            distcity = [ ]
            dc = District_city.objects.all()
            for i in dc:
                if district == i.district:
                    distcity.append(i.city)
            return render(request,'dtoclab.html',{'distcity':distcity,'lab_name':lab_name,'type_of_test':type_of_test,'email':email,'phone':phone,'address':address,'district':district,'photo':photo,'certificate':certificate})
        else:
            

            print(lab_name)
            print(type_of_test)
            print(email)
            print(phone)
            print(city)
            print(district)
            print(photo)
            print(certificate)


            lab = Laboratory(id=current_user.id,Lab_name=lab_name,phone=phone,email=email,address=address,city=city,district=district,lab_photo=photo,certificate=certificate)
            lab.save()
            labtype = lab_type(lab_id=current_user.id,test_type=type_of_test)
            labtype.save()
            profile = Profile.objects.get(id=current_user.id)
            profile.user = "laboratory"
            profile.save()

            return redirect('home')




def lab_register(request):
    print("complited")

    if request.method == "POST":
        print('in')

        current_user = request.user

        lab_name = request.POST['lab_name']
        type_of_test = request.POST['type_of_test']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        district = request.POST['district']
        photo = request.FILES['photo']
        certificate = request.FILES['certificate']

        
        if current_user.username == phone:  
            if photo is None or certificate is None:
                messages.info(request,'choose the photo')
                return redirect('lab_register')
            elif len(str(lab_name)) < 1:
                messages.info(request,'please fileup the lab name')
                return redirect('lab_register')
            elif lab_name[0] == ' ':
                messages.info(request,'space in lab name')
                return redirect('lab_register')
            elif len(str(type_of_test)) < 1:
                messages.info(request,'please fileup the lab name')
                return redirect('lab_register')
            elif type_of_test[0] == ' ':
                messages.info(request,'space in lab name')
                return redirect('lab_register')
            elif len(str(address)) < 1:
                messages.info(request,'please fileup the lab name')
                return redirect('lab_register')
            elif address[0] == ' ':
                messages.info(request,'space in lab name')
                return redirect('lab_register')
            elif len(str(district)) < 1:
                messages.info(request,'please fileup the lab name')
                return redirect('lab_register')
            elif district[0] == ' ':
                messages.info(request,'space in lab name')
                return redirect('lab_register')
            else:

                data = [lab_name,type_of_test,email,phone,address,district,photo,certificate]
                distcity = [ ]
                dc = District_city.objects.all()
                for i in dc:
                    if district == i.district:
                        distcity.append(i.city)
                return render(request,'dtoclab.html',{'distcity':sorted(distcity),'lab_name':lab_name,'type_of_test':type_of_test,'email':email,'phone':phone,'address':address,'district':district,'photo':photo,'certificate':certificate})


                return redirect('home')

            return redirect('lab_register')
       
        else:
            messages.info(request,'Phone Number not matched')
        
            return redirect('lab_register')
        

    else:
        dc = District_city.objects.all()
        district_data = [ ]
        for i in dc:
            district_data.append(i.district)

        return render(request,'lab_register.html',{'district_data':sorted(list(set(district_data)))})



def show(request):

    
    data = Laboratory.objects.all()
    
    for d in data:

        if d.id == 14:
            return render(request,'base.html',{'dataimg':d})
    
        
    

    return render(request,'base.html')



def search_lab(request):

    lab = request.POST['lab']

    labs = Laboratory.objects.all()
    test = lab_type.objects.all()
    test_id = [ ]
    dist = [ ]
    new_labs = [ ]

    for i in test:

        if lab == i.test_type:
            test_id.append(i.lab_id)

    tests,district,city = data()

    for t in test:
        if lab == t.test_type:
            for l in labs:
                if t.lab_id == l.id:
                    dist.append(l.district)


    for i in labs:
        for j in set(test_id):
            if i.id == j:
                new_labs.append(i)


    return render(request,'laboratory.html',{'lab':new_labs,'test':test,'lab_for_district':lab,'id':set(test_id),'dist':set(dist),'city':set(city),'tests':set(tests)})


def search_district_lab(request):

    dist = request.POST['dist']
    lab_for_district = request.POST['lab_for_district']
    
  

    lab = Laboratory.objects.all()
    test = lab_type.objects.all()

    test_id = [ ]
    new_test_id = [ ]
    newlab = [ ]
    district = [ ]
    city = [ ]
    tests = [ ]

    for i in test:
        if lab_for_district == i.test_type:
            test_id.append(i.lab_id)

    for i in lab:
        print(".......done......")
        print(dist)
        print(i.district)
        if dist == i.district:
            print('.....ok......')
            for j in test_id:
                if i.id == j:
                    newlab.append(i)
                    new_test_id.append(j)


    for t in test:
        if lab_for_district == t.test_type:
            for l in lab:
                if t.lab_id == l.id:
                    district.append(l.district)
                    


    for c in newlab:
        city.append(c.city)

    for t in test:
        tests.append(t.test_type)

    print(request.POST['dist'])


    return render(request,'laboratory.html',{'lab':newlab,'test':test,'lab_for_district':lab_for_district,'district_for_city':dist,'id':set(new_test_id),'dist':set(district),'city':set(city),'tests':set(tests)})



def search_city_lab(request):

    lab_for_district = request.POST['lab_for_district']
    print(".........",lab_for_district)
    city = request.POST['city']
    print(city)
    district_for_city = request.POST['hello']
    print(district_for_city)

    lab = Laboratory.objects.all()
    test = lab_type.objects.all()

    tests = [ ]
    tests1 = [ ]
    dist = [ ]
    cities = [ ]
    lab1 = [ ]
    lab2 = [ ]
    lab3 = [ ]

    for t in test:
        if lab_for_district == t.test_type:
            tests.append(t.lab_id)
            

    for l in lab:
        for t in tests:
            if l.id == t:
                lab1.append(l)
                dist.append(l.district)

    for l in lab1:
        if district_for_city == l.district:
            lab2.append(l)
            cities.append(l.city)

    for l in lab2:
        if city == l.city:
            lab3.append(l)

    for t in test:
        tests1.append(t.test_type)

    
    return render(request,'laboratory.html',{'lab':lab3,'test':test,'lab_for_district':lab_for_district,'district_for_city':district_for_city,'dist':set(dist),'city':set(cities),'tests':set(tests1)})



def labiddata(request):
    
    id = request.GET['id']

    print(id)

    return render(request,'laboratory.html',{'block13':"block",'id':id})



def labtakeappoint(request):

    current_user = request.user
    id = request.GET['id']
    date = request.GET['date']

    print(id)
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
    print(x.date())



    appoint_list = Lab_appointment_list(appointment_no=no.data,user_id=current_user.id,lab_id=id,date=x.date())
    new_appoint = new_Doctors_Appointment(patient_id=user.id,name=user.first_name+" "+user.last_name,dob=profile.date_of_birth,phone=user.username,email=user.email,date=x,address=profile.Address,zip_code=profile.pin,language=profile.languages,blood=profile.blood_group,appointment_no=no.data)
    new_appoint.save()
    appoint_list.save()
    no.save()

    return redirect('laboratory')



