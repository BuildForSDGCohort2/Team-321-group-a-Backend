from django.urls import path, include
from .views import SpecialistView

urlpatterns = [
    path('',SpecialistView, name='specialist')
]