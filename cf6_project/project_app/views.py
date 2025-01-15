from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models

# Create your views here.
def home(request):
    to_do = models.To_do.objects.all()
    context = {
        'to_do': to_do
    }
    return render(request, "project_app/home.html", context)

class ToDoListView(ListView):
    model = models.To_do
    template_name = 'project_app/home.html'
    context_object_name = 'to_do'

class ToDoDetailView(DetailView):
    model = models.To_do

class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = models.To_do
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.To_do
    fields = ['title', 'description']

    def test_func(self):
        to_do = self.get_object()
        return self.request.user == to_do.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ToDoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.To_do
    success_url = reverse_lazy('project_home')

    def test_func(self):
        to_do = self.get_object()
        return self.request.user == to_do.author

def about(request):
    return render(request, "project_app/about.html")