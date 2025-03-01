# homework/forms.py
from django import forms
from .models import Homework

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['subject', 'title', 'description', 'due_date', 'is_finished']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject...'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_finished': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
