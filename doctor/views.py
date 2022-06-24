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
                doc_username = "John",
                time = request.GET[slot]
            )
            appt+=1
           

            fs.save()
            

    #testing
    for i in Free_Slots.objects.all():
        print(i.doc_username, i.time)

    return render(request,"doctor/free_slots_doc.html")
