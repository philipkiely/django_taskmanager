# How to create an API with Django 2.2

Philip Kiely

Introduction
* Define an API, API versus website
* Why write an API: think about the client. Note that I usually write APIs as backends for mobile apps and web services, so I implement it like a backend and less like a traditional API. Not a comprehensive guide.
* Define tools: JSON, Django, djangorestframework (briefly touch on REST)
* Two ways to interact with the API: DRF and Postman

Example Project: ToDo manager, the perennial classic of tutorial writers worldwide
* / lists available endpoints
* /signin logs in users
* /getobjects gets all tasks for user (task is foreign-keyed)
* /putobject creates a new task for the user
* /postobject updates a task by id for the user
* /deleteobject deletes an task by id for the user

Summary: something

An API, or Application Programming Interface, is a broadly defined area of backend development. Essentially, the API we will write today is a website without the frontend, instead of rendering html pages, this backend returns data in the JSON format for use in native or web applications. Just like when creating a website, the most important thing to consider when writing an API is how it will be used. Today, we will discover how to use Django to create an API for a basic todo application.
Following this tutorial will require a few tools. You should have Python 3, Django 2.2, and djangorestframework installed in a virtual environment (see the official documentation or run `pip install -r requirements.txt`). Also, you'll want to download the free version of Postman installed. Postman is an excellent tool for developing and testing APIs, and we will only scratch the surface of its features. Finally, you're welcome to develop the project from scratch or clone it from [this GitHub repository.]
To start, navigate to the taskmanager directory that contains `manage.py` and run the command `python manage.py migrate` to apply the database migrations to the sqlite database. Then, run `python manage.py runserver`.
There are two ways to interact with the API: the djangorestframework templates and making http requests. Open your web browser and navigate to `127.0.0.1:8000`, or localhost at port 8000, where Django projects run by default. You should see a webpage showing a list of available API endpoints. This is an important principle in the REST approach to APIs: the API itself should show users whats available and how to use it.
