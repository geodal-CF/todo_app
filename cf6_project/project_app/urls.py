from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoListView.as_view(), name="project_home"),    # Home page: Displays a list of all To-Do items
    path('todo/<int:pk>/', views.ToDoDetailView.as_view(), name="project_detail"),  # Detail page: Displays details of a specific To-Do item identified by its primary key (pk)
    path('todo/create/', views.ToDoCreateView.as_view(), name="project_create"),    # Create page: Allows users to create a new To-Do item
    path('todo/<int:pk>/update', views.ToDoUpdateView.as_view(), name="project_update"),    # Update page: Allows users to update an existing To-Do item identified by its primary key (pk)
    path('todo/<int:pk>/delete', views.ToDoDeleteView.as_view(), name="project_delete"),    # Delete page: Allows users to delete an existing To-Do item identified by its primary key (pk)
    path('about/', views.about, name="project_about"),   # About page: Displays information about the To-Do app
]
