from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    Specialisation = models.CharField(max_length=255,default='')
    Aadhaar_ID = models.CharField(max_length=12,default='')

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialisation = models.CharField(max_length=255)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    aadhaar_id = models.CharField(max_length=12)

