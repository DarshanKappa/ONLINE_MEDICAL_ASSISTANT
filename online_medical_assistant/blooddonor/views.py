from django.shortcuts import render
from account.models import Profile
from django.contrib.auth.models import User

# Create your views here.


def blood_donor(request):

    user = User.objects.all()
    profile = Profile.objects.all()
    bg = [ ]
    district = [ ]
    city = [ ]

    for i in profile:
        bg.append(i.blood_group)

    for i in profile:
        district.append(i.district)

    for i in profile:
        city.append(i.city)




    return render(request,'blood_donor.html',{'profile':profile,'user':user,'bg':set(bg),'district':set(district),'city':sorted(list(set(city)))})



def search_bg(request):

    bg = request.POST['bg']

    profile = Profile.objects.all()
    user = User.objects.all()

    profile1 = [ ]
    user1 = [ ]
    bg1 = [ ]
    district = [ ]
    city = [ ]


    for i in profile:
        if bg == i.blood_group:
            profile1.append(i)
        bg1.append(i.blood_group)
        district.append(i.district)
        city.append(i.city)

    for i in user:
        for j in profile1:
            if i.id == j.id:
                user1.append(i)




    return render(request,'blood_donor.html',{'profile':profile1,'user':user1,'bg_for_city':bg,'bg':set(bg1),'district':set(district),'city':sorted(list(set(city)))})



def search_district_bg(request):
    
    bg = request.POST['bg']
    district = request.POST['district']

    profile = Profile.objects.all()
    user = User.objects.all()

    profile1 = [ ]
    user1 = [ ]
    bg1 = [ ]
    district1 = [ ]
    city = [ ]

    for i in profile:
        if bg == i.blood_group:
            district1.append(i.district)
            if district == i.district:
                profile1.append(i)
                city.append(i.city)
        bg1.append(i.blood_group)


    for i in profile1:
        for j in user:
            if i.id == j.id:
                user1.append(j)



    return render(request,'blood_donor.html',
                {
                'profile':profile1,
                'user':user1,
                'bg_for_city':bg,
                'district_for_city':district,
                'bg':set(bg1),
                'district':set(district1),
                'city':sorted(list(set(city)))
                })


def search_city_bg(request):

    bg = request.POST['bg']
    district = request.POST['district']
    city = request.POST['city']

    profile = Profile.objects.all()
    user = User.objects.all()

    profile1 = [ ]
    user1 = [ ]
    bg1 = [ ]
    district1 = [ ]
    city1 = [ ]

    for i in profile:
        bg1.append(i.blood_group)
        if bg == i.blood_group:
            district1.append(i.district)
            if district == i.district:
                city1.append(i.city)
                if city == i.city:
                    profile1.append(i)

    for i in profile1:
        for j in user:
            if i.id == j.id:
                user1.append(j)

    

    return render(request,'blood_donor.html',
                {
                'profile':profile1,
                'user':user1,
                'bg_for_city':bg,
                'district_for_city':district,
                'bg':set(bg1),
                'district':set(district1),
                'city':sorted(list(set(city1)))
                })
