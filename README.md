### BUILDING STUDENT MANAGEMENT SYSTEM USING DJANGO V3.2


### 1. SETUP
###---------


#### 1.1 Complate basic setup: project, app, db and hello world

        new file:   .gitignore
        new file:   README.md
        new file:   apps/main/__init__.py
        new file:   apps/main/admin.py
        new file:   apps/main/apps.py
        new file:   apps/main/migrations/__init__.py
        new file:   apps/main/models.py
        new file:   apps/main/templates/main/index.html
        new file:   apps/main/tests.py
        new file:   apps/main/urls.py
        new file:   apps/main/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


### 2. DJANGO ADMIN ACTIVATION
###---------------------------


#### 2.1 Create superuser

        (venv3932) λ python manage.py migrate
        (venv3932) λ python manage.py createsuperuser


### 3. TEMPLATING AND STATIC FILES
###-------------------------------


#### 3.1 Adding template to home page and load static files

        modified:   README.md
        modified:   apps/main/templates/main/index.html

        NOTE: 

        Static files are ignored by git


#### 3.2 Templates inheritance

        modified:   README.md
        modified:   apps/main/templates/main/index.html
        new file:   templates/base.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header.html
        new file:   templates/shared/scripts.html
        new file:   templates/shared/sidebar.html


### 4. CREATING MORE APPS
###----------------------


#### 4.1 Create student app

        modified:   README.md
        new file:   apps/student/__init__.py
        new file:   apps/student/admin.py
        new file:   apps/student/apps.py
        new file:   apps/student/migrations/__init__.py
        new file:   apps/student/models.py
        new file:   apps/student/tests.py
        new file:   apps/student/views.py
        modified:   config/settings.py


#### 4.2 Create staff app

        modified:   README.md
        new file:   apps/staff/__init__.py
        new file:   apps/staff/admin.py
        new file:   apps/staff/apps.py
        new file:   apps/staff/migrations/__init__.py
        new file:   apps/staff/models.py
        new file:   apps/staff/tests.py
        new file:   apps/staff/views.py


#### 4.3 Create hod app

        modified:   README.md
        new file:   apps/hod/__init__.py
        new file:   apps/hod/admin.py
        new file:   apps/hod/apps.py
        new file:   apps/hod/migrations/__init__.py
        new file:   apps/hod/models.py
        new file:   apps/hod/tests.py
        new file:   apps/hod/views.py
        modified:   apps/staff/apps.py
        modified:   config/settings.py


#### 4.4 Create user app

        modified:   README.md
        new file:   apps/user/__init__.py
        new file:   apps/user/admin.py
        new file:   apps/user/apps.py
        new file:   apps/user/migrations/__init__.py
        new file:   apps/user/models.py
        new file:   apps/user/tests.py
        new file:   apps/user/views.py
        modified:   config/settings.py


### 5. USER: LOGIN, REGISTER, LOGOUT
###---------------------------------


#### 5.1 Login Part 1 - Create login page TVUrl

        modified:   README.md
        new file:   apps/user/templates/user/login.html
        new file:   apps/user/urls.py
        modified:   apps/user/views.py
        modified:   config/urls.py
        modified:   templates/shared/header.html


#### 5.2 Login Part 2 - Removed social login and forgot password form login page 

        modified:   README.md
        modified:   apps/user/templates/user/login.html