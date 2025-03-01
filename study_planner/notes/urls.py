# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),                   # The main list + create
    path('<int:pk>/', views.notes_detail, name='notes-detail'),
    path('<int:pk>/edit/', views.notes_edit, name='notes-edit'),
    path('<int:pk>/delete/', views.notes_delete, name='notes-delete'),
]
