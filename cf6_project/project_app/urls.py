from django.urls import path
from . import views

'app/model_viewtype'
'project/project_detail.html'

urlpatterns = [
    path('', views.ToDoListView.as_view(), name="project_home"),
    path('todo/<int:pk>/', views.ToDoDetailView.as_view(), name="project_detail"),
    path('todo/create/', views.ToDoCreateView.as_view(), name="project_create"),
    path('todo/<int:pk>/update', views.ToDoUpdateView.as_view(), name="project_update"),
    path('todo/<int:pk>/delete', views.ToDoDeleteView.as_view(), name="project_delete"),
    path('about/', views.about, name="project_about"),
]
