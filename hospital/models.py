from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Doctor(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    RANK_CHOICES = [
        ('Consultant', 'Consultant'),
        ('Specialist', 'Specialist'),
        ('Senior Registrar', 'Senior Registrar'),
        ('Registrar', 'Registrar'),
    ]

    SPECIALTY_CHOICES = [
        ('IMC', 'IMC'),
        ('Surgery', 'Surgery'),
        ('OBG', 'OBG'),
        ('Pedia', 'Pedia'),
        ('Ortho', 'Ortho'),
        ('Nepherology', 'Nepherology'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES)

    def __str__(self):
        return self.name
