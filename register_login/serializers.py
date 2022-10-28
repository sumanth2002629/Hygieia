from rest_framework import serializers
from . models import User,Doctor,Patient

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        depth = 1

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1