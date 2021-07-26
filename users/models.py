from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('Erkek','Erkek'),
        ('Kadın','Kadin'),
    )
    bio = models.CharField(max_length=1000,null=True, blank=True)
    gender = models.CharField(max_length=100, choices = GENDER_CHOICES, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    birthdate = models.DateField(null=True,blank=True)