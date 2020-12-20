# from django.contrib import messages, auth
# from django.shortcuts import render, redirect, HttpResponse
# from .form import UserForm, BaseForm
# from .models import BaseUser
# from django.contrib.auth.models import User
#
# # Create your views here.
# def home(requests):
#     form = UserForm
#     baseform = BaseForm
#     if requests.method == 'POST':
#         username = requests.POST['username']
#         email = requests.POST['email']
#         password1 = requests.POST['password1']
#         password2 = requests.POST['password2']
#         phone_number = requests.POST['phone_number']
#
#
#         if len(password1) >= 8 and password1 == password2:
#             if len(phone_number) < 11 or len(phone_number) > 15:
#
#                 return HttpResponse('enter the correct phone number')
#             else:
#                 try:
#                     user = User.objects.get(username= username)
#                     return HttpResponse('user already exist')
#                 except User.DoesNotExist:
#                     reuser = User.objects.create_user(username=username, email=username, password = password1)
#                     phone_number = requests.POST['phone_number']
#                     user_type = requests.POST['user_type']
#                     if user_type == '':
#                         user_type == 'patient'
#
#
#                     BaseUser.objects.create(user_type = user_type, user = reuser, phone_number = phone_number )
#                     auth.login(requests, reuser)
#                     return HttpResponse('sign up successfully')
#         else:
#             messages.success(requests, "place make sure your password is up 8 mixed value")
#             context = {'form': form,
#                        'baseform': baseform}
#             return render(requests, 'hospital/home.html', context)
#         # form = UserForm(requests.POST)
#         # baseform = BaseForm(requests.POST, instance=requests.user.baseuser)
#         # if form.is_valid() and baseform.is_valid():
#         #     user = form.save()
#         #     baseform = baseform.save(commit=False)
#         #     baseform.user = user
#         #     baseform.save()
#         #     return HttpResponse('successful sign up')
#
#
#
#     context = {'form': form,
#                'baseform':baseform}
#     return render(requests, 'hospital/home.html', context)
from base64 import b64decode

import jwt
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, LoginSerializer, AppointmentSerializer, \
    SpecialistSerializer, SpecialistUpdateSerializer, HospitalSerializer, UserSerializer3
from django.contrib import auth
from django.conf import settings
from .permissions import IsPatientUserType, IsDoctorUserType
from .models import User, Appointment, Specialist, Hospital
from rest_framework.decorators import action


@api_view(['GET'])
def current_user(request, token):
    """
    Determine the current user by their token, and return their data
    """
    # data = {'user': serializer.data, 'token': auth_token}
    #
    # return Response(data, status=status.HTTP_200_OK)

    try:
        data = jwt.decode(token, (settings.JWT_SECRET_KEY))
        user = User.objects.get(username=data['username'])
        serializer = UserSerializer(user)

        data = {'user': serializer.data}

        return Response(data, status=status.HTTP_200_OK)

    except jwt.DecodeError:
        return JsonResponse({'error': 'user does not exist'})

        # raise e("Invalid token")
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class RegisterView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    queryset = User.objects.all()

    def post(self, request):

        data = request.data
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            user_type = serializer.validated_data.get('user_type')
            good = data.get('is_patient')

            if user_type == 'specialist':
                # User.is_patient = False
                # serializer.save(is_patient=False)
                print('do nothing')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        usser = User.objects.all()
        serializer = UserSerializer(usser, many=True)
        return Response(serializer.data)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Appointment.objects.all()

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print('user', user)
        print('username', username)
        print('password', password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # def get(requests, token):
        #
class HospitalView(GenericAPIView):
    serializer_class = HospitalSerializer

    # def get(self, request):
    #     hospital = Hospital.objects.all()
    #     serializer = HospitalSerializer(hospital)
    #     return Response(serializer.data)
    def post(self, request):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            serializer.save()
            # print('it entered validation')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Hospital.objects.all()

    def get(self, request):
        hospital = Hospital.objects.all()
        serializer = HospitalSerializer(hospital, many=True)
        return Response(serializer.data)


class AppointmentView(GenericAPIView):
    permission_classes = (IsAuthenticated, IsPatientUserType)
    serializer_class = AppointmentSerializer

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            serializer.save(user_name=self.request.user)
            # print('it entered validation')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print('couldnt make it')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        usser = Appointment.objects.filter(user_name=self.request.user)
        serializer = UserSerializer(usser)
        return Response(serializer.data)


class SpecialistAppointmentView(GenericAPIView):
    serializer_class = SpecialistSerializer
    permission_classes = (permissions.AllowAny,)
    # lookup_field = "id"
    queryset = Specialist.objects.all()

    # this method will help in calling a particular user_type
    # def get(self, request):
    #     specialist = Specialist.objects.filter(user_type='specialist')
    #     serializer = SpecialistSerializer(specialist, many=True)
    #     return Response(serializer.data)
    def get(self, request):
        specialist = Specialist.objects.all()
        serializer = SpecialistSerializer(specialist, many=True)
        return Response(serializer.data)


class AppointmentList(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsDoctorUserType)

    def perform_create(self, serializer):
        serializer.save(user_name=self.request.user)

    def get_queryset(self):
        return Appointment.objects.filter(specialist=self.request.user)


class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated, IsPatientUserType)
    lookup_field = "id"

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user.id)


class SpecialistUpdateView(APIView):
    # permission_classes = (permissions.IsAuthenticated, IsDoctorUserType)
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def get(self,  doctor_id):
        try:
            model = Specialist.objects.get(user_id=doctor_id)
        except Specialist.DoesNotExist:
            return Response(f'doctor with the id {doctor_id} is not found', status=status.HTTP_404_NOT_FOUND)
        serializer = SpecialistUpdateSerializer(model)
        return Response(serializer.data)

    # parser_classes = (MultiPartParser, FormParser,)
    # parser_classes = (FormParser,)
    def patch(self, request, doctor_id):
        model = Specialist.objects.get(user_id=doctor_id)
        data = request.data
        #nested object updated
        user = User.objects.get(id=doctor_id)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.gender = data.get('gender', user.gender)
        user.save()
        # model.user = user
        model.profile_picture = data.get('profile_picture', model.profile_picture)
        try:
            hospital = Hospital.objects.get(id=data['hospital'])
            model.hospital = hospital
        except KeyError:
            pass
        model.user = data.get('user', model.user)
        model.description = data.get('description', model.description)
        model.save()
        serializer = SpecialistUpdateSerializer(model)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# using this method for updating nested serialized data, sets the data on a different endpoint. this is not what we want
#     @action(detail=True, methods=['patch'])
#     def specialist_profile(self, request, pk=None):
#         user = self.get_objects()
#         profile = user.specialist
#         serializer = UserSerializer3(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_409_CONFLICT)



