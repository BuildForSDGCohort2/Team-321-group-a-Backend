from os import path
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import HospitalSerializer, SpecialistSerializer, DoctorSerializer, UserSerializer, AppointmentSerializer, PaymentSerializer
from .models import Hospital, Specialist, Doctor, User, Appointment, Payment

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

def index(requets):
    return HttpResponse("Hello world")