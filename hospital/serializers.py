from rest_framework import serializers
from .models import Hospital, User, Specialist, Doctor

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
