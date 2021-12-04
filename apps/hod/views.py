# apps/hod_page/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def hod_home(request):
	return render(request, 'hod/home.html')