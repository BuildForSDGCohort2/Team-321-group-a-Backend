from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

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


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.hospital_name

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hospital = models.ManyToManyField(Hospital)
    description = models.TextField()

    def __str__(self):
        return f'{self.user}'

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hospital = models.ManyToManyField(Hospital)
    description = models.TextField()


