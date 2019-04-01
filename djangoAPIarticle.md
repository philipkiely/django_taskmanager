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
