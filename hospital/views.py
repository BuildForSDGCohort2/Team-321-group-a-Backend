from os import path
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import HospitalSerializer
from .models import Hospital

class HospitalView(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()

def SpecialistView(request):
    return HttpResponse("Hello world")