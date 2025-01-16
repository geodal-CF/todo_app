from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):      # Custom form to handle user registration
  email = forms.EmailField()                   # Add an email field to the default UserCreationForm

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']