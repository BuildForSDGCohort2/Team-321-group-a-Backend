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
    message = 'Permission denied, you are not a specialist'

    def has_permission(self, request, view):
        # request.user checks your program authentication mode(user). This
        # permission's checks that a user making the request must be a specialist
        # user_type only
        if request.user.user_type == 'specialist':
            return True


class IsSpecialistAndPatient(BasePermission):
    message = 'permission denied, you are neither a patient or a specialist'

    def has_permission(self, request, view):
        if request.user.user_type == 'specialist' or request.user.user_type == 'patient':
            return True
