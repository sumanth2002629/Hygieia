from xml.etree.ElementTree import fromstring
from django.shortcuts import render
from doctor.models import Free_Slots

# Create your views here.

def home(request):
    return render(request, 'doctor/home.html')

def add_slots(request):
    print(request.GET)
    if request.GET:
        appt=0
        for slot in request.GET:
            print(type(request.GET[slot]))
            print(request.GET["appt"+str(appt)])
            fs = Free_Slots(
                doc_username = "John",#hard coded for now. get it from logged in user
                time = request.GET[slot]
            )
            appt+=1
           

            fs.save()
            

    #testing
    for i in Free_Slots.objects.all():
        print(i.doc_username, i.time)

    return render(request,"doctor/free_slots_doc.html")

def view_slots(request):
    #get username actually from cookie or something
    username= "John"
    available =  Free_Slots.objects.filter(doc_username=username)
    return render(request, 'doctor/view_slots.html',{"available":available})
