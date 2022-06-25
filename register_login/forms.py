from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from register_login.models import (User,Doctor,Patient)

class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        User._meta.get_field('email')._unique = True
        fields=['username','email','password1','password2','Specialisation']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor(user=user)
        doctor.specialisation = self.cleaned_data.get('Specialisation')
        doctor.save()
        return user

class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        User._meta.get_field('email')._unique = True
        fields=['username','email','password1','password2','Aadhaar_ID']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient(user=user)
        patient.aadhaar_id = self.cleaned_data.get('Aadhaar_ID')
        patient.save()
        return user

