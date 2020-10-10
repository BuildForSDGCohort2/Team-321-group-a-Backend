from rest_framework.permissions import BasePermission


class IsPatientUserType(BasePermission):
    message = 'Permission denied, you are not a patient'
    def has_permission(self, request, view):
        # request.user checks your program authentication mode(user). This
        # permisssion cheecks that a user making the request must be a patient
        # user_type only
        if request.user.user_type == 'patient':
            return True

class IsDoctorUserType(BasePermission):
    message = 'Permission denied, you are not a Doctor'
    def has_permission(self, request, view):
        # request.user checks your program authentication mode(user). This
        # permisssion cheecks that a user making the request must be a patient
        # user_type only
        if request.user.user_type == 'doctor':
            return True
