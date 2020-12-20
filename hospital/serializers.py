from .models import Hospital, User, Specialist, Appointment, Payment, Company, SpecialistType

from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import User


# from rest_framework.authtoken.models import Token

# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#
#         model = User
#         fields = ('id', 'username', 'email', 'password')
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone_number', 'user_type',
                  ]

    # fields = ['username', 'first_name', 'last_name', 'email', 'password'
    #                   ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ("Email is already in use, don't leave field empty")})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class AppointmentSerializer(serializers.ModelSerializer):
    # reschedule_startime = serializers.DateTimeField(read_only=True)
    # reschedule_endtime = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Appointment
        fields = ['specialist', 'user_name', 'day', 'start_time', 'end_time',
                  'Aim', 'alert',
                  ]


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        models = Appointment
        fields = '__all__'


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['user_id', 'hospital', 'description', 'profile_picture']
        depth = 1
        # read_only_fields = ['user']


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'Address']

class UserSerializer3(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'id', 'first_name', 'last_name','gender',  'phone_number'
                         ]
        read_only_fields = ['id']


class SpecialistUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer3(required=True)

    class Meta:
        model = Specialist
        # read_ = ['user', ]
        fields = ['user', 'hospital', 'description', 'profile_picture']
        # read_only_fields = ['user']
        # depth = 1

    # def update(self, instance, validated_data):
    #     nested_serializer = self.fields['user']
    #     nested_instance = instance.user
    #     nested_data = validated_data.pop('profile')
    #     nested_serializer.update(nested_instance, nested_data)
    #     return super(SpecialistUpdateSerializer, self).update(instance, validated_data)
    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = UserSerializer.update(UserSerializer(), validated_data=user_data)
    #     instance.user = validated_data.get(instance.user)
    #     instance.hospital = validated_data.get('hospital', instance.hospital)
    #     instance.description = validated_data.get('hospital', instance.description)
    #     instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
    #     instance = super().update(instance, validated_data)
    #     instance.save()
    #     return instance
