This symbol "--" represents a topic.
This symbol "-" represents an explanation of the topic

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

Version 1.0.4
Author: Josaiah Saldana
Date: 1/30/2025

**What I Learned**

-- LoginRequireMixin | from django.contrib.auth.mixins import LoginRequireMixin

- This is a way to ensure that users can manipulate what they are allowed to manipulate only if they are logged into their account.

--LOGIN_URL = 'login' | settings.py

- This is used to redirect users to the login page if they try to access a part that they are not allowed to access due to the LoginRequireMixin.

-- get_context_data

- Is used to override the default get_context_data method.

-- context = super().get_context_data(\*\*kwargs)

- This is used to trigger the function belonging to the super parent to gather data. kwargs is used to pass additional parameters.

-- context['tasks'] = context['tasks'].filter(user=self.request.user)

- This is used to filter the tasks that are shown only to their respective users. Users will not be allowed to see tasks that are not their own.

-- context['count'] = context['tasks'].filter(complete=False).count()

- This adds a new count key that will keep track of the number of incomplete tasks.

-- def form_valid(self, form):
form.instance.user = self.request.user
return super(TaskCreate,self).form_valid(form)

- The purpose of this method is to automatically assign a task to the current logged in user instead of allowing them to choose the user.

Version 1.0.5
Author: Josaiah Saldana
Date: 2/1/2025

Updated pages with style header

Version 1.0.6
Author: Josaiah Saldana
Date: 2/1/2025

**What I Learned**

--<form method="GET">
<input type="text" name="search-area" value="{{search_input}}">
<input type="submit" value="Search">

  </form>
 This form implements a search feature for tasks using a GET request. When the user submits the form, the text they type into the input field is sent to the server as a URL parameter. The name attribute of the input (search-area) acts as the key in this URL parameter, and the search term they typed becomes the value associated with that key. The server uses this key-value pair to find and return matching tasks.

--search_input = self.request.GET.get('search-area') or ''

- Used to retrieve the contents of the GET request. It also handles if the GET request is empty

--if search_input:
context['tasks'] = context['tasks'].filter(
title\_\_startswith=search_input)
context['search_input'] = search_input

- If the search_input is not empty, the code will filter out the tasks using the search_input variable. We then ensure that the html file is able to recognize the {{search_input}} and replace it with the value.

Version 1.0.7
Author: Josaiah Saldana
Date: 2/1/2025
Branch: Register/main

**What I Learned**

-- FormView | from django.views.generic.edit import FormView

- Form view is a way to render forms that will be used for submissions.

-- UserCreationForm | from django.contrib.auth.forms import UserCreationForm

- Django form designed to for user registration.

-- form_class

- Attribute that indicates what form a view should use.

-- def form_valid(self, form):
user=form.save()
if user is not None:
login(self.request, user)
return super(RegisterPage, self).form_valid(form)

- user=form.save() saves the data from the form to the database which creates a new user. The if statement checks if the user already exists within the database. login will automatically login the user if they already exist. Super is called to complete the default behavior of the method is executed.

-- def get(self, *args, \*\*kwargs):
if self.request.user.is_authenticated:
return redirect('tasks')
return super(RegisterPage,self).get(*args, \*\*kwargs)

- This simply redirects the user if the user is already logged in with an account. We call super to ensure the default behavior is completed .get(\*args, \*\*kwargs) with the new information.
