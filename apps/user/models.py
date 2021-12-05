# apps/user/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser  

# Locals

# Create your models here.

class CustomUserModel(AbstractUser):

	USER = (
		(1, 'Hod'),
		(2, 'Staff'),
		(3, 'Student'),
	)

	user_type = models.CharField(choices=USER,max_length=50,default=1)
	profile_pic = models.ImageField(upload_to='images/profile_pic')

