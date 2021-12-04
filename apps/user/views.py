# apps/user/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def user_login(request):
	return render(request, 'user/login.html')

