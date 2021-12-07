# apps/student/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Locals
from apps.student.models import Course, Session_Year
from apps.user.models import CustomUserModel
from apps.student.models import Student  

# Create your views here.


# Add student ----------------------------------------------------
@login_required(login_url='user:user_login')
def add_student(request):

	# 1. First thing first: fetch the course and session_year
	courses = Course.objects.all()
	session_years = Session_Year.objects.all()

	# Testing
	# print(courses)
	# print(session_years)

	# 2. Add logic if there is request method of POST to process the form input
	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		gender = request.POST.get('gender')
		address = request.POST.get('address')
		course_id = request.POST.get('course_id')
		session_year_id = request.POST.get('session_year_id')
		email = request.POST.get('email')
		username = request.POST.get('username')
		password = request.POST.get('password')

		# Testing
		# print(profile_pic, first_name, last_name, gender, address, course_id, session_year_id, email, username, password)
		# result
		# contact01.PNG teststudent1 teststudent1 Female teststudent1 1 1 teststudent1@email.com teststudent1 teststudent1

		# 3. Check the existance of email and username in the db bc they are unique
		#    send messages if any of them is exists in the db
		
		# 3.1 Check existance of the email (email=unique)
		if CustomUserModel.objects.filter(email=email).exists():
			messages.warning(request, 'Email is already taken !')
			return redirect('student:add_student')

		# 3.1 Check existance of username (email=unique)
		if CustomUserModel.objects.filter(username=username).exists():
			messages.warning(request, 'Username is already in used !')
			return redirect('student:add_student')

		# 4. Process the request if email and username are not exists in the db
		else:
			user = CustomUserModel(
				profile_pic=profile_pic,
				first_name = first_name,
				last_name  = last_name,
				username   = username,
				email 	   = email,
				user_type  = 3,
			)
			user.set_password(password)
			user.save()

			# 5. Making TWO in ONE: Student as user and Student's choice for course and session_year
			course = Course.objects.get(id=course_id)
			session_year = Session_Year.objects.get(id=session_year_id)

			student = Student(
				admin = user,
				gender = gender,
				address = address,
				course_id = course,
				session_year_id = session_year
			)

			student.save()
			messages.success(request, user.first_name + " " + user.last_name + ' Added successfully!')
			# messages.success(request, 'Student added successfully!')
			return redirect('student:add_student')
			# 5. end Making TWO in ONE: Student as user and Student's choice for course and session_year

	context = {
		'courses':courses,
		'sessions':session_years
	}
	return render(request, 'student/add-student.html', context)


	''' NOTE about adding student as user as well as as student

		1. First thing first: fetch the course and session
		2. Add logic if there is request method of POST to process the form input
		3. Check the existance of email and username in the db bc they are unique
		   send messages if any of them is exists in the db
		4. Process the request if email and username are not exists in the db
		5. Making TWO in ONE: Student as user and Student's choice for course and session_year
	
	'''


# Add student end ----------------------------------------------------
