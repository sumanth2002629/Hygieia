from xml.etree.ElementTree import fromstring
from django.shortcuts import render
from doctor.models import Free_Slots
from register_login.models import Doctor,Patient

# Create your views here.

def home(request):
    user = request.user
    doctor = Doctor.objects.filter(user=user)
    return render(request, 'doctor/doctor_profile.html',{"doctor":doctor[0]})

def add_slots(request):
    print(request.GET)
    if request.GET:
        appt=0
        for slot in request.GET:
            print(type(request.GET[slot]))
            print(type(slot))
            print(request.GET["appt"+str(appt)])
            fs = Free_Slots(
                doc_username =  request.user.username,#hard coded for now. get it from logged in user
                time = request.GET[slot]
            )
            appt+=1
           

            fs.save()
            

    #testing
    for i in Free_Slots.objects.all():
        print(i.doc_username, i.time,i.id,i.is_booked,i.patient_name)

    return render(request,"doctor/free_slots_doc.html")

def view_slots(request):
    #get username actually from cookie or something
    print(request.GET)
    # print(request.POST)


    if "apptno" in request.GET:
        Free_Slots.objects.get(id=int(request.GET['apptno'])).delete()

    username= request.user.username
    
    available =  Free_Slots.objects.filter(doc_username=username)
    return render(request, 'doctor/view_slots.html',{"available":available})