from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoctorSignUpForm, PatientSignUpForm
from .models import User, Doctor, Patient
from .serializers import DoctorSerializer,PatientSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def signup_doctor(request):

    print(request.data)
    
    form = DoctorSignUpForm(data=request.data) 
    if form.is_valid():
        form.save()

        Response("Thank you for registering!!")

        return redirect('login') #This needs to be removed later.


@api_view(['POST'])
def signup_patient(request):
    
    
    form = PatientSignUpForm(request.POST)
    if form.is_valid():
        form.save()

        Response("Thank you for registering!!")
        return redirect('login') #This needs to be removed later

    else:
        form = PatientSignUpForm()
        return Response(form.errors.as_data())
    


@api_view(['GET'])
def profile(request):
    if not request.user.is_authenticated:
        return Response("User is not authenticated!!")

    serializer = DoctorSerializer(request.user,many=False)
    return Response(serializer.data)

    # if Doctor.objects.filter(user=request.user):
    #     details = Doctor.objects.get(user=request.user)
    #     serializer = DoctorSerializer(details,many=False)
        
    #     return Response(serializer.data)
    #     # return redirect('doctor-home')
    # else:
    #     details = Patient.objects.get(user=request.user)
    #     serializer = PatientSerializer(details,many=False)
    #     return Response(serializer.data)
    #     # return redirect('patient-home')