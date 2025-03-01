# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('<int:pk>/update/', views.todo_update, name='todo-update'),
    path('<int:pk>/delete/', views.todo_delete, name='todo-delete'),
    path('<int:pk>/complete/', views.todo_complete, name='todo-complete'),
]
