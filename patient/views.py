from django.shortcuts import render,redirect
from django.core.mail import send_mail
from register_login.models import Doctor,User,Patient
from doctor.models import Free_Slots
import random,string


# Create your views here.


def home(request):
    user = request.user
    patient = Patient.objects.filter(user=user)
    return render(request, 'patient/patient_profile.html',{"patient":patient[0]})

def book_appoinment(request):
    #first recieve specialisation and sort doctors based on that

    if "name" in request.GET:#chosen a doctor
        doc_name = request.GET["name"]
        # print(request.GET["apptno"])
        return patient_view_slots(request,doc_name)
        # return redirect("patient_view_slots" ,{"doc_no":doc_no})

    d = Doctor.objects.all()
    for i in d:
        print(i.user.username,i.specialisation)

    if "specialisation" in request.GET:#searching based on specialisation
        print("searching")
        d=d.filter(specialisation = request.GET["specialisation"])

    if "apptno" in request.GET:#they have chosen a slot
        print(request.GET['apptno'])
        slot = Free_Slots.objects.get(id=int(request.GET['apptno']))
        print(slot)
        slot.is_booked = True
        slot.patient_name = request.user.username
        slot.room_id = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 6))
        slot.save()
        subject = "Hygiea: Room Id for video call"
        message = "Hello sir/ma'am,\n This email is to provide you with the room id for ur appoinment with Dr. "+slot.doc_username+" on "+str(slot.time)+"\n Room ID: "+slot.room_id
        patient_emailid = User.objects.get(username = slot.patient_name).email
        print(patient_emailid)
        send_mail (
            subject,
            message,
            "hygieahh2@outlook.com",
            [patient_emailid],
            fail_silently=False,


        )
    #     send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )

        return redirect("patient-home")
        


    return render(request, 'patient/book_appoinment.html',{"available_doctors":d})

def patient_view_slots(request,doc_name):

    # print(request.GET)
    # doc = User.objects.get(username = doc_name)
    
    print(doc_name)
    available =  Free_Slots.objects.filter(doc_username=doc_name)
    available = available.filter(is_booked=False)
    print(available)
    return render(request, 'patient/patient_view_slots.html',{"available_slots":available})