# apps/student/views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Locals

# Create your views here.


# Add student
@login_required(login_url='user:user_login')
def add_student(request):
	context = {}
	return render(request, 'student/add-student.html', context)


