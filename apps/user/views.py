# apps/user/views.py

# Django modules
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout, login

# Locals
from apps.user.EmailBackEnd import EmailBackEnd 

# Create your views here.

def user_login(request):
	return render(request, 'user/login.html')

def doLogin(request):

	if request.method == 'POST':
		user = EmailBackEnd.authenticate(request,
										 username=request.POST.get('email'),
										 password=request.POST.get('password'))

		if user != None:
			login(request,user)
			user_type = user.user_type

			if user_type == '1':
				return HttpResponse('This is HOD Panel')

			elif user_type == '2':
				return HttpResponse('This is Staff Panel')

			elif user_type == '3':
				return HttpResponse('This is Student Panel')

			else:
				# message
				return redirect('user:user_login') 

		else:
			# message
			return redirect('user:user_login')

	# return None

