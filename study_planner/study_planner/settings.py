# import os
# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-your-secret-key-here'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.sites', 
#     # Required for django-allauth
#     # Required for django-allauth
# 'crispy_bootstrap4',
#     # Third-party apps
#     'crispy_forms',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',

#     # Local apps
#     'dashboard',
#     'notes',
#     'homework',
#     'todo',
#     'resources',
#     'users',
#     'widget_tweaks',
# ]
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'allauth.account.middleware.AccountMiddleware',  # Add this line
# ]


# ROOT_URLCONF = 'study_planner.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, "templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',  # Required by allauth
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'study_planner.wsgi.application'

# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

# # Internationalization
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Add this line

# # Media files configuration
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # Login URL configuration
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'profile'

# # Message framework settings
# from django.contrib.messages import constants as messages
# MESSAGE_TAGS = {
#     messages.DEBUG: 'alert-secondary',
#     messages.INFO: 'alert-info',
#     messages.SUCCESS: 'alert-success',
#     messages.WARNING: 'alert-warning',
#     messages.ERROR: 'alert-danger',
# }

# # Default primary key field type
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # Crispy Forms
# CRISPY_TEMPLATE_PACK = "bootstrap4"

# # django-allauth settings
# SITE_ID = 1  # Required for django-allauth

# AUTHENTICATION_BACKENDS = [
#     # Django's default authentication backend
#     "django.contrib.auth.backends.ModelBackend",
    
#     # Allauth-specific authentication methods
#     "allauth.account.auth_backends.AuthenticationBackend",
# ]

# ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_EMAIL_REQUIRED = False



# LOGOUT_REDIRECT_URL = '/dashboard/'  # Replace with your dashboard URL


import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)
# Read the .env file in the project root
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# You can optionally set allowed hosts via env variable; default is empty list
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-allauth

    # Third-party apps
    'crispy_bootstrap4',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'users',
    # Local apps
    'dashboard',
    'notes',
    'homework',
    'todo',
    'resources',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this if required by your allauth setup
]

ROOT_URLCONF = 'study_planner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'study_planner.wsgi.application'

# Database configuration loaded from .env; e.g., DATABASE_URL=sqlite:///db.sqlite3
DATABASES = {
    'default': env.db(),
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Login URL configuration
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'

# Message framework settings
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Crispy Forms settings
CRISPY_TEMPLATE_PACK = "bootstrap4"

# django-allauth settings
SITE_ID = 1  # Required for django-allauth

AUTHENTICATION_BACKENDS = [
    # Django's default authentication backend
    "django.contrib.auth.backends.ModelBackend",
    # Allauth-specific authentication method
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = False

LOGOUT_REDIRECT_URL = '/dashboard/'

# Additional project-specific settings loaded from the environment
STUDY_PLANNER_ENV = env('STUDY_PLANNER_ENV')
