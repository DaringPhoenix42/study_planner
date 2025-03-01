# notes/models.py
from django.db import models

class Note(models.Model):
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('Study', 'Study'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='General'
    )
    tags = models.CharField(
        max_length=200,
        blank=True,
        help_text='Comma-separated tags (e.g. "django, python, tutorial")'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
