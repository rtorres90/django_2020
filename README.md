# django_2020

## Steps made.

#. ``django-admin startproject meeting-planner``
#. ``python manage.py startapp website`` to create an app to just handle the static web pages. 


## Notes.

#. To see the needed migrations run ``python manage.py showmigrations``
#. To apply the migration ``python manage.py migrate``
#. To add an app ``python manage.py startapp meetings``
#. To make migrations after modify the models ``python manage.py startapp meetings``
#. To apply the migrations created ``python manage.py sqlmigrate meetings 0001``
#. Then after those steps ``python manage.py migrate``