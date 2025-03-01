# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']






# users/forms.py

# users/forms.py

# users/forms.py

# users/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Add some Bootstrap classes
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'




# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'profile_pic']
#         widgets = {
#             'bio': forms.Textarea(attrs={'rows': 4}),
#         }

# users/forms.py

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'profile_pic']
