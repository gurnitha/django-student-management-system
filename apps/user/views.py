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
def profile(request):
	return render(request, 'user/profile.html')


# User profile create
def profile_update(request):
	user = CustomUserModel.objects.get(id=request.user.id)
	print(user)
	context = {'user':user}
	return render(request, 'user/profile-update.html', context)
