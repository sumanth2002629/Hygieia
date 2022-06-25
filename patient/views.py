from time import thread_time
from django.shortcuts import render
from register_login.models import Doctor

# Create your views here.


def home(request):
    return render(request, 'patient/home.html')

def book_appoinment(request):
    #first recieve specialisation and sort doctors based on that

    d = Doctor.objects.all()
    for i in d:
        print(i.user.username,i.specialisation)

    if "specialisation" in request.GET:
        print("searching")
        d=d.filter(specialisation = request.GET["specialisation"])

    return render(request, 'patient/book_appoinment.html',{"available_doctors":d})
