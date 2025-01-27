Version 1.0.0
Author: Josaiah Saldana
Date: 1/27/2025

**What I learned**

-- DetailView from django.views.generic.detail import DetailView

- DetailView is a class based view that displays a detail view of a single object from a database. For DetailView, django looks for a template with a prefix of the name of the mode and a suffix of \_detail.html. In order to properly implement DetailView, we must add a class in the views file of the app and include "DetailView" in the inheritance parentheses. This allows the new class to gain the functionality of DetailView. We then create a url path in urls.py in the app. DetailView works on a key:value basis. So the url must include something like 'task/<int:pk>/

-- context_object_name

- context_object_name is an attribute that can be defined in a class based view to specify the name of a variable that will be used to pass the object from the view template. I used it to specify the name of some class based view to something like 'task'.

-- CreateView | from django.views.generic.edit import CreateView

- CreateView is a class based view that is designed to handle the creation of new objects in the database. The process is simplified by rendering a form, validating user input, saving data to the database and redirecting the user after a successful submission. Django expects the default template named task_form.html. We create a class for it in views.py in the app and specify the CreateView attribute in the inheritance paremeter.

-- reverse_lazy | Django.urls import reverse_lazy

- Reverse_lazy is a way to redirect the user to another url after a succesful submission. The parameter that is required for the reverse_lazy method is a url string. Specifically, a url string from the urls.py. We use reverse_lazy in class attributes because it delays URL resolution until needed.
