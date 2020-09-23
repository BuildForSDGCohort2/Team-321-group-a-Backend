from rest_framework import serializers
from .models import Hospital, User, Specialist, Doctor, Appointment, Payment, Company, SpecialistType

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = '__all__'

class SpecialistTypeSerializer(serializers.Serializer):
    class Meta:
        model = SpecialistType
        fields = '__all__'