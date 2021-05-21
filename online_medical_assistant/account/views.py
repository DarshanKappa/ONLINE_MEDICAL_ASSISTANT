from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from home.views import home
from .models import Profile
from .forms import Student
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from data.models import District_city

@ensure_csrf_cookie
@csrf_protect



# Create your views here.

def districttocity(request):

    if request.method == "POST":

        first_name = request.POST['first']
        last_name = request.POST['last']
        date = request.POST['date']
        languag = request.POST['lang']
        blood = request.POST['blood']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        pin = request.POST['pin']
        city = request.POST['city']
        district = request.POST['dist']
        password1 = request.POST['pass']

        if len(str(city)) < 1 :
            data = [first_name,last_name,date,languag,blood,gender,email,phone,address,pin,district,password1]
            messages.info(request,"please select a city")
            return render(request,'districttocity.html',{'data':data})
        else:
            print(first_name)
            print(last_name)
            print(date)
            print(languag)
            print(blood)
            print(gender)
            print(email)
            print(address)
            print(pin)
            print(city)
            print(district)
            print(password1)
           
            user = User.objects.create_user(username=phone,password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print('user created.........')
            data = User.objects.all()
            for d in data:
                if d.username == phone:
                    print(d.id)
                    print(d.username)
                    profile = Profile(id=int(d.id),date_of_birth=date,languages=languag,blood_group=blood,gender=gender,Address=address,pin=pin,city=city,district=district,photo='media/lab_photo/destination_2.jpg')
                    profile.save()
            return redirect('login')


    
    
    return render(request,'districttocity.html')


def register(request):

    st = Student()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date = request.POST['date']
        languag = request.POST['languag']
        blood = request.POST['blood']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        pin = request.POST['pin']
        district = request.POST['district']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
            if len(str(first_name)) < 1: 
                messages.info(request,'please fillup First Name')
                return redirect('register') 
            elif first_name[0] == ' ':
                messages.info(request,"first letter is ' ' (spance) ")
                return redirect('register')          
            elif len(str(last_name)) < 1: 
                messages.info(request,'please fillup larst Name')
                return redirect('register') 
            elif last_name[0] == ' ':
                messages.info(request,"first letter is ' ' (spance) ")
                return redirect('register')          
            elif len(str(blood)) < 1: 
                messages.info(request,'please fillup Blood Group')
                return redirect('register') 
            elif blood[0] == ' ':
                messages.info(request,"first letter is ' ' (spance) ")
                return redirect('register')          
            elif len(str(email)) < 1: 
                messages.info(request,'please fillup Email')
                return redirect('register') 
            elif email[0] == ' ':
                messages.info(request,"first letter is ' ' (spance) ")
                return redirect('register')          
            elif len(str(phone)) > 10 or len(str(phone)) < 10:
                messages.info(request,'mobile number must be 10')
                return redirect('register')
            elif User.objects.filter(username=phone).exists():
                messages.info(request,'mobile number taken')
                return redirect('register') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register') 
            elif len(str(district)) < 1:
                messages.info(request,'District is empty')
                return redirect('register') 
            else:
                # print(first_name)
                # print(last_name)
                # print(date)
                # print(languag)
                # print(blood)
                # print(gender)
                # print(email)
                # print(address)
                # print(pin)
                
                # print(district)
                # print(password1)
                data = [first_name,last_name,date,languag,blood,gender,email,phone,address,pin,district,password1]
                distcity = [ ]
                dc = District_city.objects.all()
                for i in dc:
                    if district == i.district:
                        distcity.append(i.city)

                return render(request,'districttocity.html',{'distcity':sorted(distcity),'first_name':first_name,'last_name':last_name,'date':date,'languag':languag,'blood':blood,'gender':gender,'address':address,'email':email,'phone':phone,'pin':pin,'district':district,'password1':password1})


        else:
            messages.info(request,'confirm password not matched')
            return redirect('register')
        return redirect('login')
    else:
        dc = District_city.objects.all()
        district_data = [ ]
        for i in dc:
            district_data.append(i.district)
            
        return render(request,'registration.html',{'form':st,'district_data':sorted(list(set(district_data)))})


def login(request):

    if request.method == 'POST':
        print(".........post accepted........")
        username = request.POST['phone']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            print("........login..........")
            auth.login(request, user)
            data = User.objects.all()
            for d in data:
                if d.username == username:
                    data = d.first_name
            return render(request,'home.html',{'display':'none','account':True,'data':data})
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        
    else:
        print(".......post not accepted........")
        return render(request,'home.html',{'display':'block','account':False})



def logout(request):
    auth.logout(request)
    return render(request,'home.html',{'display':'none'})


