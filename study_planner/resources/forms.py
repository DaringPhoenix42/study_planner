# # resources/forms.py
# from django import forms
# from .models import Book, WikiResource, YouTubeVideo

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'description', 'link', 'rating']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'link': forms.URLInput(attrs={'class': 'form-control'}),
#             'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
#         }

# class WikiForm(forms.ModelForm):
#     class Meta:
#         model = WikiResource
#         fields = ['title', 'url', 'snippet', 'rating']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'url': forms.URLInput(attrs={'class': 'form-control'}),
#             'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
#         }

# class YouTubeForm(forms.ModelForm):
#     class Meta:
#         model = YouTubeVideo
#         fields = ['title', 'channel', 'link', 'description', 'rating']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'channel': forms.TextInput(attrs={'class': 'form-control'}),
#             'link': forms.URLInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
#         }






# resources/forms.py
from django import forms
from .models import Book, WikiResource, YouTubeVideo

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'link', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

class WikiForm(forms.ModelForm):
    class Meta:
        model = WikiResource
        fields = ['title', 'url', 'snippet', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

class YouTubeForm(forms.ModelForm):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'channel', 'link', 'description', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'channel': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
