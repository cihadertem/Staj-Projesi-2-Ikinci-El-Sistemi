from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('Erkek','Erkek'),
        ('Kadın','Kadin'),
        ('Belirtilmedi', 'Belirtilmedi'),
    )
    bio = models.CharField(max_length=1000,null=True, blank=True,default="Henüz bir biyografi girilmedi...")
    gender = models.CharField(max_length=100, choices = GENDER_CHOICES, null=True, blank=True,default='Belirtilmedi')
    avatar = models.ImageField(null=True, blank=True, default='klasikpp.jpg')
    birthdate = models.DateField(null=True,blank=True,default='2000-01-01')