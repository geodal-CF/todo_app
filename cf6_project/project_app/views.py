from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models

# Create your views here.
# Function-based view for the home page
def home(request):
    to_do = models.To_do.objects.all()  # Retrieves all To-Do items from the database
    context = {                         # Passes the items to the template as context
        'to_do': to_do
    }
    return render(request, "project_app/home.html", context)

# Class-based view to display a list of all To-Do items
class ToDoListView(ListView):
    model = models.To_do
    template_name = 'project_app/home.html'
    context_object_name = 'to_do'

# Class-based view to display details of a single To-Do item
class ToDoDetailView(DetailView):
    model = models.To_do

# Class-based view to handle the creation of a new To-Do item
class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = models.To_do
    fields = ['title', 'description']

    # Sets the author of the To-Do item to the currently logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class-based view to handle the updating of an existing To-Do item
class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.To_do
    fields = ['title', 'description']

    # Ensures only the author of the To-Do item can update it
    def test_func(self):
        to_do = self.get_object()
        return self.request.user == to_do.author

    # Sets the author of the To-Do item to the currently logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class-based view to handle the deletion of an existing To-Do item    
class ToDoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.To_do
    success_url = reverse_lazy('project_home')

    # Ensures only the author of the To-Do item can delete it
    def test_func(self):
        to_do = self.get_object()
        return self.request.user == to_do.author

# Function-based view for the About page
def about(request):
    return render(request, "project_app/about.html")