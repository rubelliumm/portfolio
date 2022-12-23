from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_home, name='todo_homepage_url'),
    path('del/<int:pk>', views.remove_todo, name='delete_todo_url'),
    path('add/', views.add_todo, name='add_todo_url'),
    path('edit/<int:pk>', views.edit_todo, name='edit_todo_url'),
]
