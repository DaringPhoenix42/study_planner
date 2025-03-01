# resources/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view, name='books'),
    path('wikipedia/', views.wikipedia_view, name='wikipedia'),
    path('youtube/', views.youtube_view, name='youtube'),
]
