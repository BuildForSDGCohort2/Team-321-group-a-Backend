from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Payment(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('M', 'Mastercard'),
        ('V', 'Visa'),
    ]
    Account_name = models.CharField(max_length=20, help_text="Enter the name for account")
    Account_type = models.CharField(max_length=3,choices=ACCOUNT_TYPE_CHOICES, help_text="Choose a type for the card")
    Account_number = models.IntegerField()
    Account_password = models.CharField(max_length= 20 ,help_text="Enter the password")
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
      (1, 'patient'),
      (2, 'specialist'),
      (3, 'doctor'),
      (4, 'admin'),
      (5, 'technician'),
  )
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    gender = models.CharField(max_length=2, help_text="Enter gender", choices=SEX_CHOICES)
    date_of_birth = models.DateField(help_text="Enter the date of birth", null=True,blank=True)
    date_of_death  = models.DateField(help_text="Enter the date of death", null=True, blank=True)
    Address = models.CharField(max_length=100, help_text="Enter the address", null=True),
    Image = models.ImageField(upload_to='user-images', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    account = models.ForeignKey(Payment, on_delete=models.CASCADE, help_text="The account details", blank=True, null=True)

    def __str__(self):
        return self.username

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.hospital_name



class SpecialistType(models.Model):
    SPECIALIST_TYPE_LIST = [
        ('F','Freelance'),
        ('H','Hospital'),
    ]
    specialist_category = models.CharField(max_length=20, help_text="Enter the type of specialist")
    specialist_type = models.CharField(max_length=2, help_text="The type of specialist",choices=SPECIALIST_TYPE_LIST)

    def __str__(self):
        return self.specialist_category

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    specialist_type = models.ForeignKey(SpecialistType, help_text="choose the type of specialist", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.user}'

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hospital = models.ManyToManyField(Hospital)
    description = models.TextField()

    def __str__(self):
        return f'{self.user}'

class Appointment(models.Model):

    ALLERT_TYPE = [
        ('L', 'Low'),
        ('M','Medium'),
        ('H','High')
    ]

    VENUE_LIST = [
        ('A', 'Hospital'),
        ('B', 'Home'),
        ('C', 'Online')
    ]
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    venue = models.CharField(max_length=2,choices=VENUE_LIST, default='H',  help_text="The venue for appointment")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    Aim = models.TextField()
    alert = models.CharField(max_length=2, choices=ALLERT_TYPE, help_text="Choose the type of alert", blank=True, null=True)
    user_doctor = models.ForeignKey(Doctor, help_text="Choose the doctor", on_delete=models.CASCADE, null=True, blank=True)
    user_specialist = models.ForeignKey(Specialist, help_text="Choose the Specialist", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.venue
