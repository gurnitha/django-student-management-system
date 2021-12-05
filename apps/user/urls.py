# apps/user/urls.py

# Django modules
from django.urls import path

# Locals
from apps.user import views 

app_name = 'user'

urlpatterns = [

    # Login template
    path('', views.user_login, name='user_login'),
    # User login
    path('doLogin/', views.doLogin, name='doLogin'),
    # User logout
    path('doLogout/', views.doLogout, name='doLogout'),
    # User profile
    path('profile/', views.profile, name='profile'),
]