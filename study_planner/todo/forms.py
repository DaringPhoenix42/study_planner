# todo/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'priority', 'due_date', 'is_finished']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Todo title...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Details...'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_finished': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
