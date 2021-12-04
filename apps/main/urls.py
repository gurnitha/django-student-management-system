# apps/main/urls.py

# Django modules
from django.urls import path

# Locals
from apps.main import views 

app_name = 'main'

urlpatterns = [

    path('', views.home, name='home'),
    
]