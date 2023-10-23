# todoapp/urls.py
from django.urls import path
from .views import todo_list, delete_todo, mark_completed

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('mark_completed/<int:todo_id>/', mark_completed, name='mark_completed'),
]
