# apps/hod_page/views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Locals

# Create your views here.
@login_required(login_url='user:user_login')
def hod_home(request):
	return render(request, 'hod/home.html')

