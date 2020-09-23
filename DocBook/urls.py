from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hospital import views

router = routers.DefaultRouter()
router.register(r'hospitals', views.HospitalView, 'hospital')
router.register(r'specialist', views.SpecialistView, 'specialist')
router.register(r'doctors', views.DoctorView, 'doctor')
router.register(r'users', views.UserView,'user')
router.register(r'appointment', views.AppointmentView, 'appointment')
router.register(r'payment', views.PaymentView, 'payment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('api/',include(router.urls))
]