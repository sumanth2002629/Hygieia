from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoctorSignUpForm, PatientSignUpForm
from .models import User, Doctor, Patient


def signup_doctor(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = DoctorSignUpForm()

    return render(request, 'register_login/signup_doctor.html', {'form': form})


def signup_patient(request):
    
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = PatientSignUpForm()

    return render(request,'register_login/signup_patient.html',{'form':form})

    



def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'register_login/login.html')

    username = request.user.username

    if Doctor.objects.filter(user=request.user):
        # Go to recruiter home page

        details = Doctor.objects.get(user=request.user)
        return redirect('doctor-home')
    else:
        # pass
        #change this to patient
        details = Patient.objects.get(user=request.user)
        return redirect('patient-home')