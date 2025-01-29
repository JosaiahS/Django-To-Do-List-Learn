Version 1.0.0
Author: Josaiah Saldana
Date: 1/27/2025

**What I learned**

-- DetailView from django.views.generic.detail import DetailView

- DetailView is a class based view that displays a detail view of a single object from a database. For DetailView, django looks for a template with a prefix of the name of the mode and a suffix of \_detail.html. In order to properly implement DetailView, we must add a class in the views file of the app and include "DetailView" in the inheritance parentheses. This allows the new class to gain the functionality of DetailView. We then create a url path in urls.py in the app. DetailView works on a key:value basis. So the url must include something like 'task/<int:pk>/

-- context_object_name

- context_object_name is an attribute that can be defined in a class based view to specify the name of a variable that will be used to pass the object from the view template. I used it to specify the name of some class based view to something like 'task'. Only affects the variable name used in the template.

-- CreateView | from django.views.generic.edit import CreateView

- CreateView is a class based view that is designed to handle the creation of new objects in the database. The process is simplified by rendering a form, validating user input, saving data to the database and redirecting the user after a successful submission. Django expects the default template named task_form.html. We create a class for it in views.py in the app and specify the CreateView attribute in the inheritance paremeter.

-- reverse_lazy | Django.urls import reverse_lazy

- Reverse_lazy is a way to redirect the user to another url after a succesful submission. The parameter that is required for the reverse_lazy method is a url string. Specifically, a url string from the urls.py. We use reverse_lazy in class attributes because it delays URL resolution until needed.

-- <a href="{% url 'task-create' %}"> Add Task</a>

- {% url 'task-create' %} This is a Django template tag that dynamically generates the URL for the named URL pattern 'task-create'. Djnaog looks in the urls.py and replaces that tag with the actual URL path. href creates a hyperlink. The 'Add Task' part of the code is what the text that is displayed to the user.

Version 1.0.1
Author: Josaiah Saldana
Date: 1/27/2025

**What I Learned**

-- <form method="POST" action="">
<input type="submit" value="Submit" />

</form>

- A django template tag that is used to specify that a HTTP POST request will be sent. The 'input type='submit' creates a submit button that submits the form data to the server when clicked. value ="Submit" is the text that will appear inside the submit box.

-- {% csrf_token %}

- A security measure that protects against malicious cross site request forgery.

-- {{form.as_p}}

- Django tag that wraps the form fields as paragraphs. Makes it easier to edit the form.

-- UpdateView | from django.views.generic.edit

- A django class based view designed to update objects created utilizing the CreateView class based view. It used the same form as the CreateView which is '(name_of_app)\_form.html'

Version 1.0.2
Author: Josaiah Saldana
Date: 1/29/2025

**What I Learned**

--DeleteView | from django.views.generic.edit import DeleteView

- A django class based view designed to delete objects from database. Django expects a POST request from a template/base html called "name_of_app_confirm_delete.html". It is implemented vy creating a class based view in views.py, creating a url in urls.py, creating a POST request on task_confirm_delete.html and then updating task_list.html.

Version 1.0.3
Author: Josaiah Saldana
Date: 1/29/2025

**What I Learned**

-- LoginView | from django.contrib.auth.views import LoginView

- LoginView is a django class based view that has much of the functionality for login built-in. Allowing simpler implementation of login functionality. Django LoginView by default expects a template called 'login.html' where a form post request will be implemented for the login.

-- LogoutView | from django.contrib.auth.views import LogoutView

- LogoutView is a django class based view that allows for simpler implementation of logout functionality. It used to work for both get and post requests until Django 4.1 which only allows by default post requests for logoutview for security reasons such as csrf.
