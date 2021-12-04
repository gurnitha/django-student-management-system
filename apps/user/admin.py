# apps/user/admin.py

# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  

# Locals
from apps.user.models import CustomUserModel

class UserModelAdmin(UserAdmin):
	list_display = ['username', 'user_type']

# Register your models here.
admin.site.register(CustomUserModel, UserModelAdmin)