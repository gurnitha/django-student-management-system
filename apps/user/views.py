# apps/user/views.py

# Django modules
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Locals
from apps.user.EmailBackEnd import EmailBackEnd 
from apps.user.models import CustomUserModel

# Create your views here.

# Login template
def user_login(request):
	return render(request, 'user/login.html')


# User login
def doLogin(request):

	if request.method == 'POST':
		user = EmailBackEnd.authenticate(request,
										 username=request.POST.get('email'),
										 password=request.POST.get('password'))

		if user != None:
			login(request,user)
			user_type = user.user_type

			if user_type == '1':
				# return HttpResponse('This is HOD Panel')
				return redirect('hod:hod_home')

			elif user_type == '2':
				return HttpResponse('This is Staff Panel')

			elif user_type == '3':
				return HttpResponse('This is Student Panel')

			else:
				# message
				messages.error(request, 'Invalid email or password!')
				return redirect('user:user_login') 

		else:
			# message
			messages.error(request, 'Invalid email or password!')
			return redirect('user:user_login')


# User logout
def doLogout(request):
	logout(request)
	return redirect('user:user_login')


# User profile
@login_required(login_url='user:user_login')
def profile(request):

	user = CustomUserModel.objects.get(id=request.user.id)

	# print(user)
	
	context = {'user':user}
	return render(request, 'user/profile.html', context)


# User profile update
@login_required(login_url='user:user_login')
def profile_update(request):

	if request.method == 'POST':
		profile_pic = request.FILES.get('profile_pic')
		first_name  = request.POST.get('first_name')
		last_name   = request.POST.get('last_name')
		# email  		= request.POST.get('email')
		# username  	= request.POST.get('username')
		password  	= request.POST.get('password')

		# testing
		print(profile_pic)
		# print(first_name, last_name, password)
		# print(profile_pic, first_name, last_name, email, username, password)

		try:
			customuser = CustomUserModel.objects.get(id=request.user.id)

			customuser.first_name 	= first_name
			customuser.last_name 	= last_name
			# customuser.username 	= username
			# customuser.profile_pic 	= profile_pic
			
			if password != None and password != "":
				customuser.set_password(password)

			if profile_pic != None and profile_pic != "":
				customuser.profile_pic = profile_pic

			customuser.save()

			messages.success(request, 'Profile updated successfully!')
			# redirect('user:profile_update')
			# return redirect('hod:hod_home')
			return redirect('user:profile')
			# return redirect('user:profile_update')

		except:
			messages.error(request, 'Failed to update Profile!')

	context = {}
	return render(request, 'user/profile.html', context)
