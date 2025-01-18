from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from . import forms

# Register view: Handles user registration process
def register(request):
  if request.method == "POST":
    form = forms.UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')    # a dictionary of validated form input fields and their values, where the username is returned as an object
      messages.success(request, f"{username}, your account has been created! Please log in.")
      return redirect('user-login')
  else:
    # if the form is not valid, user input is kept and the process can be continued until the form is valid
    form = forms.UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

# Logout view: Logs the user out and renders a logout page
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

# Profile view: Displays the user's profile page
def profile(request):
  return render(request, 'users/profile.html')

# Profile view (protected): Requires user to be logged in to access
@login_required
def profile(request):
  return render(request, 'users/profile.html')