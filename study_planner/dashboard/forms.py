# dashboard/forms.py
from django import forms
from .models import Note, Homework, Todo

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
