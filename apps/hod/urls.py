# apps/hod/urls.py

# Django modules
from django.urls import path

# Locals
from apps.hod import views 

app_name = 'hod'

urlpatterns = [

    path('hod/', views.hod_home, name='hod_home'),
    
]