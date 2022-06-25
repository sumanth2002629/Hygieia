from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoctorSignUpForm,PatientSignUpForm
from .models import User,Doctor,Patient

def signup_doctor(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('base-home')

    else:
        form = DoctorSignUpForm()

    return render(request,'register_login/signup_doctor.html',{'form':form})

def signup_patient(request):
    form1 = PatientSignUpForm(request.POST)
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()

            return redirect('base-home')
        else:
            form1 = PatientSignUpForm()

    return render(request,'register_login/signup_patient.html',{'form':form1})

    






