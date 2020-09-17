from django.contrib import admin
from .models import User, Hospital, Specialist, Doctor, Appointment

# Register your models here.

#admin.site.register(User)
#admin.site.register(Hospital)
#admin.site.register(Specialist)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','gender')
admin.site.register(User, UserAdmin)

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('user','description')
admin.site.register(Specialist,SpecialistAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name','Address')
admin.site.register(Hospital, HospitalAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment,AppointmentAdmin )