# apps/student/urls.py

# Django modules
from django.urls import path

# Locals
from apps.student import views 

app_name = 'student'

urlpatterns = [

    path('student/add-student/', views.add_student, name='add_student'),
    
]