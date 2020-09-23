from os import path
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import HospitalSerializer, SpecialistSerializer, DoctorSerializer, UserSerializer, AppointmentSerializer, PaymentSerializer, CompanySerializer, SpecialistTypeSerializer
from .models import Hospital, Specialist, Doctor, User, Appointment, Payment, Company, SpecialistType

class HospitalView(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()

class SpecialistView(viewsets.ModelViewSet):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()


class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AppointmentView(viewsets.ModelViewSet):
    serializer_class  = AppointmentSerializer
    queryset = Appointment.objects.all()

class PaymentView(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class SpecialistTypeView(viewsets.ModelViewSet):
    serializer_class = SpecialistTypeSerializer
    queryset = SpecialistType.objects.all()

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

def index(requets):
    return HttpResponse("Hello world")