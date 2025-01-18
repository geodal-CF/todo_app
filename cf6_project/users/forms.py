from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):      # Custom form to handle user registration
  email = forms.EmailField()                   # Adds an email field to the default UserCreationForm

  class Meta:   # built-in configuration class used to change the behavior of a model
    model = User
    fields = ['username', 'email', 'password1', 'password2']    # specifies what custom fields will be shown and in what order