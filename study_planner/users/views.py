# # from django.shortcuts import render, redirect
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib import messages

# # def register(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             messages.success(request, f'Account created for {username}! You can now log in.')
# #             return redirect('login')
# #     else:
# #         form = UserCreationForm()
# #     return render(request, 'users/register.html', {'form': form})


# # from django.shortcuts import render
# # from django.contrib.auth.decorators import login_required

# # @login_required
# # def profile(request):
# #     return render(request, 'users/profile.html')



# # from django.shortcuts import render
# # from django.contrib.auth.decorators import login_required

# # @login_required
# # def profile(request):
# #     return render(request, 'users/profile.html')









# # # users/views.py

# # from django.shortcuts import render, redirect
# # from django.contrib import messages
# # from django.contrib.auth import login
# # from django.contrib.auth.views import LoginView, LogoutView
# # from django.urls import reverse_lazy
# # from django.contrib.auth.decorators import login_required

# # from .forms import UserRegisterForm

# # def register(request):
# #     if request.method == 'POST':
# #         form = UserRegisterForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             # Auto-login the user after registration
# #             login(request, user)
# #             messages.success(request, 'Account created successfully!')
# #             return redirect('dashboard')  # or wherever you want
# #     else:
# #         form = UserRegisterForm()
# #     return render(request, 'users/register.html', {'form': form})


# # class CustomLoginView(LoginView):
# #     template_name = 'users/login.html'
# #     # Optionally, you can specify success_url or redirect_authenticated_user here
# #     # e.g. success_url = reverse_lazy('dashboard')


# # class CustomLogoutView(LogoutView):
# #     # By default, LogoutView only allows POST. We'll allow GET too:
# #     http_method_names = ['get', 'post']
# #     # Immediately redirect to 'login' after logout
# #     next_page = 'login'





# # users/views.py

# # from django.shortcuts import render, redirect
# # from django.contrib import messages
# # from django.contrib.auth import login
# # from django.contrib.auth.views import LoginView, LogoutView
# # from django.urls import reverse_lazy

# # from .forms import UserRegisterForm

# # def register(request):
# #     """
# #     Register a new user, then log them in, and redirect.
# #     """
# #     if request.method == 'POST':
# #         form = UserRegisterForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user)  # auto-login after register
# #             messages.success(request, 'Your account has been created!')
# #             return redirect('dashboard')  # or 'notes', 'homework', etc.
# #     else:
# #         form = UserRegisterForm()
# #     return render(request, 'users/register.html', {'form': form})

# # class CustomLoginView(LoginView):
# #     template_name = 'users/login.html'
# #     # success_url = reverse_lazy('dashboard')  # optional if you want a specific post-login page
# #     # redirect_authenticated_user = True       # optional

# # class CustomLogoutView(LogoutView):
# #     """
# #     By default, LogoutView in Django 5 disallows GET.
# #     We allow GET so <a href="{% url 'logout' %}"> works.
# #     Then we redirect to 'login' after logging out.
# #     """
# #     http_method_names = ['get', 'post']
# #     next_page = 'login'

# # users/views.py

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse_lazy
# from django.contrib.auth.models import User

# from .forms import UserRegisterForm

# def register_view(request):
#     """
#     Register a new user, log them in, then redirect to 'dashboard'.
#     """
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Automatically log in the user
#             login(request, user)
#             messages.success(request, 'Your account has been created!')
#             return redirect('dashboard')  # redirect to your home.html in 'dashboard'
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


# class CustomLoginView(LoginView):
#     """
#     Login with a redirect to 'dashboard' on success.
#     """
#     template_name = 'users/login.html'
#     success_url = reverse_lazy('dashboard')  # after login, go to 'dashboard'
#     # if using Django < 3.1, you might override get_success_url or set redirect_authenticated_user=True


# class CustomLogoutView(LogoutView):
#     """
#     Logout that allows GET and redirects to 'login'.
#     """
#     http_method_names = ['get', 'post']
#     next_page = 'login'

# from django.db.models.signals import post_save
# from django.dispatch import receiver





# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm


# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect('profile')
        
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful! Welcome to Study Planner.')
#             return redirect('profile')
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'users/register.html', {'form': form})

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('profile')
        
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
            
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f'Welcome back, {username}!')
                
#                 # Redirect to the page user was trying to access, or profile page
#                 next_page = request.GET.get('next', 'profile')
#                 return redirect(next_page)
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = UserLoginForm()
    
#     return render(request, 'users/login.html', {'form': form})

# @login_required
# def logout_view(request):
#     # Using POST method for logout is a security best practice
#     # This prevents CSRF attacks via GET requests
#     if request.method == 'POST':
#         logout(request)
#         messages.success(request, 'You have been logged out successfully.')
#         return redirect('login')
    
#     # If accessed via GET, show the logout confirmation page
#     return render(request, 'users/logout.html')

# @login_required
# def profile_view(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile has been updated!')
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=request.user.profile)
    
#     return render(request, 'users/profile.html', {'form': form})






from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Profile is created automatically via signals
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        # Ensure the user has a profile before proceeding
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=user)
        
        login(self.request, user)
        messages.success(self.request, f'Welcome back, {user.username}!')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    # Default template_name is already set in settings.py as LOGOUT_REDIRECT_URL
    pass

@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # Try to get profile, create if doesn't exist
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=request.user)
        
        p_form = ProfileUpdateForm(instance=profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)