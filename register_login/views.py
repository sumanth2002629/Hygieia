from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoctorSignUpForm, PatientSignUpForm
from .models import User, Doctor, Patient
from .serializers import DoctorSerializer,PatientSerializer
from django.contrib.auth.decorators import login_required

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

    else:
        form = DoctorSignUpForm()
        return Response(form.errors.as_data())


@api_view(['POST'])
def signup_patient(request):
      
    form = PatientSignUpForm(data=request.data)
    if form.is_valid():
        form.save()

        Response("Thank you for registering!!")
        return redirect('login') #This needs to be removed later

    else:
        print("Not valid")
        form = PatientSignUpForm()
        return Response(form.errors.as_data())
    

@login_required
@api_view(['GET'])
def profile(request):
    serializer = DoctorSerializer(request.user,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def login_required(request):
    return Response("Please login first to access this feature!!")





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