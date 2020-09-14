from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hospital import views

router = routers.DefaultRouter()
router.register(r'hospitals', views.HospitalView, 'hospital')
router.register(r'specialist', views.DoctorView, 'specialist')
router.register(r'doctors', views.DoctorView, 'doctor')
router.register(r'users', views.UserView,'user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('api/',include(router.urls))
]