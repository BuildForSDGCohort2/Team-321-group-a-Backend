from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Payment(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('M', 'Mastercard'),
        ('V', 'Visa'),
    ]
    Account_name = models.CharField(max_length=20, help_text="Enter the name for account")
    Account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE_CHOICES, help_text="Choose a type for the card")
    Account_number = models.IntegerField()
    Account_password = models.CharField(max_length=20, help_text="Enter the password")
    Account_pin = models.SmallIntegerField()
    Account_balance = models.IntegerField(help_text="The account balance")

    def __str__(self):
        return f'{self.Account_name, self.Account_type}'


class Company(models.Model):
    company_name = models.CharField(max_length=20, help_text="The company name")

    def __str__(self):
        return self.company_name


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'patient'),
        ('specialist', 'specialist'),
        ('doctor', 'doctor'),
        ('admin', 'admin'),
        ('technician', 'technician'),
    )
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    user_type = models.CharField(max_length=10, default='patient')
    gender = models.CharField(max_length=2, help_text="Enter gender", choices=SEX_CHOICES)
    Image = models.ImageField(upload_to='user-images/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, default='+234')

    def __str__(self):
        return self.username


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="An id of the user")
    balance = models.IntegerField(help_text="The balance")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user, self.balance


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SpecialistType(models.Model):
    SPECIALIST_TYPE_LIST = [
        ('F', 'Freelance'),
        ('H', 'Hospital'),
    ]
    specialist_category = models.CharField(max_length=20, help_text="Enter the type of specialist")
    specialist_type = models.CharField(max_length=2, help_text="The type of specialist", choices=SPECIALIST_TYPE_LIST)

    def __str__(self):
        return self.specialist_category


class Appointment(models.Model):
    ALERT_TYPE = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]

    VENUE_LIST = [
        ('Hospital', 'Hospital'),
        ('Home', 'Home'),
        ('Online', 'Online')
    ]
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    venue = models.CharField(max_length=15, choices=VENUE_LIST, default='Hospital',
                             help_text="The venue for appointment")
    day = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    Aim = models.TextField()
    alert = models.CharField(max_length=2, choices=ALERT_TYPE, help_text="Choose the type of alert", blank=True,
                             null=True)
    specialist = models.ForeignKey('Specialist', help_text="Choose the doctor", on_delete=models.CASCADE, null=True,
                                   blank=True)

    def __str__(self):
        return f'{self.specialist} {self.venue}'


class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=1, blank=True)
    description = models.TextField(blank=True)

    profile_picture = models.ImageField(upload_to='doc_image/', blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth = models.DateField(help_text="Enter the date of birth", null=True, blank=True)
    date_of_death = models.DateField(help_text="Enter the date of death", null=True, blank=True)
    Address = models.CharField(max_length=100, help_text="Enter the address", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    account = models.ForeignKey(Payment, on_delete=models.CASCADE, help_text="The account details", blank=True,
                                null=True)

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.user_type == 'patient':
        Patient.objects.get_or_create(user=instance)
    else:
        Specialist.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('_-----')
    # print(instance.internprofile.bio, instance.internprofile.location)
    if instance.user_type== 'patient':
        instance.patient_profile.save()
    else:
        Specialist.objects.get_or_create(user=instance)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print('****', created)
#     if instance.is_patient:
#         Patient.objects.get_or_create(user=instance)
#     else:
#         Specialist.objects.get_or_create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print('_-----')
#     # print(instance.internprofile.bio, instance.internprofile.location)
#     if instance.is_patient:
#         instance.patient_profile.save()
#     else:
#         Specialist.objects.get_or_create(user=instance)
