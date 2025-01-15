from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from . import forms

# Register view
def register(request):
  if request.method == "POST":
    form = forms.UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      # cleaned data is a dictionary
      username = form.cleaned_data.get('username')
      messages.success(request, f"{username}, your account has been created! Please log in.")
      return redirect('user-login')
  else:
    form = forms.UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile(request):
  return render(request, 'users/profile.html')

@login_required
def profile(request):
  return render(request, 'users/profile.html')