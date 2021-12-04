# apps/user/urls.py

# Django modules
from django.urls import path

# Locals
from apps.user import views 

app_name = 'user'

urlpatterns = [

    path('', views.user_login, name='user_login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout/', views.doLogout, name='doLogout'),
    
]