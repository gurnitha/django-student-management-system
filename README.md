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