# Django-app
Steps mentioned below are assumng you already have Python, pip and Django instaled.  

Creating a django project:
1. django-admin startproject myapp (or whatever you want to call)
2. python manage.py runserver (click on the url will show a rocket blasting off)

Creating an app inside:
1. python manage.py startapp sub_app1 (or whatever you want to call)
2. Now navigate to myapp -> settings.py
3. In INSTALLED_APPS (inside settings.py) add 'sub_app1'
