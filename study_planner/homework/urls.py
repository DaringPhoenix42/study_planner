# homework/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homework_list, name='homework'),  # instead of 'homework-list'

    path('<int:pk>/update/', views.homework_update, name='homework-update'),
    path('<int:pk>/delete/', views.homework_delete, name='homework-delete'),
    path('<int:pk>/complete/', views.homework_complete, name='homework-complete'),
]
