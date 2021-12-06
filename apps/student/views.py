# apps/student/views.py

# Django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Locals
from apps.student.models import Course, Session_Year

# Create your views here.


# Add student
@login_required(login_url='user:user_login')
def add_student(request):
	courses = Course.objects.all()
	session_years = Session_Year.objects.all()

	# Testing
	# print(courses)
	# print(session_years)

	context = {
		'courses':courses,
		'sessions':session_years
	}
	return render(request, 'student/add-student.html', context)


