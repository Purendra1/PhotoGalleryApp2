# PhotoGalleryApp2


Software Requirements to run:

-Python (3.6.x or above)

-Django (2.2.2 or above)

	pip install django
	
-Pillow

	pip install pillow
	
-Crispy

	pip install django-crispy-forms
	
-django-cleanup

	pip install django-cleanup
	
-djangorestframework

	pip install djangorestframework


To run, goto the main directory and run the following command:

	python manage.py runserver

open localhost:8000 in a web browser to access the MVC views.

open localhost:8000/api/home  to access the api views. --- 
The api views are rendered using templates so they will be visible as web pages only.
This is done for the sake of simplicity and user's convenience 
After removing the renderers from the APIViews, you can access the raw JSON responses which the Application will return.
They can be used in any other app as JSON.

I am currently developing a front end for the API of this app.
The pre-requisites are:

NodeJS (minimum v10.x.x)

	https://nodejs.org/en/download/

Angular CLI (minimum v6.x.x)

	npm install -g @angular/cli
	

