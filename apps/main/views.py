# apps/home/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

def home(request):
	return render(request, 'main/index.html')
