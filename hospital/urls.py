from . import views
from django.urls import path

from .views import RegisterView, LoginView, AppointmentView, SpecialistAppointmentView, AppointmentList, \
    AppointmentDetailView, SpecialistUpdateView, SpecialistUpdateView, HospitalView
from drf_yasg import openapi
from . import views
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Docbook Api",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    # path('', views.home, name = 'home'),

    path('register', RegisterView.as_view()),
    path('get_user/<str:token>', views.current_user, name = 'user'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('accounts/login/', LoginView.as_view()),
    path('booking',AppointmentView.as_view() ),
    path('list',AppointmentList.as_view() ),
    path('specialists',SpecialistAppointmentView.as_view() ),
    path('hospital',HospitalView.as_view() ),
    path('bookings/<int:id>',AppointmentDetailView.as_view() ),
    path('specialist/<int:doctor_id>', SpecialistUpdateView.as_view()),


]
