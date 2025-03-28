"""
Django settings for silvol project.

Generated by 'django-admin startproject' using Django 4.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@(t0gsw6_=2h3t*jfgateurlr7^&+z*k%prs-870scwv4w6pa8'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '127.0.0.1:8000',
    'silvol-3630ff49165c.herokuapp.com',
    'silvol.herokuapp.com',
    '127.0.0.1:8000/users/profile/edit/',
    '127.0.0.1:8000/users/profile/',
    '127.0.0.1:8000/availability/',
    '127.0.0.1:8000/users/profile/edit_availability/',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',
    #'allauth.socialaccount.providers.google',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',  
    'cloudinary',
    'users',
    'appointments',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'widget_tweaks',
    #'django_extensions',
] 

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1  # Required for django-allauth

LOGIN_REDIRECT_URL = 'home'  # Redirect to profile page after login  

LOGOUT_REDIRECT_URL = '/'  # Redirect after logout

# Allauth settings for email verification
ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Do not require email verification
#ACCOUNT_USERNAME_REQUIRED = False  # If you want email-only login
#ACCOUNT_SIGNUP_FIELDS = ['email', 'password1', 'password2']  # Ensure email is included for signup
#ACCOUNT_EMAIL_REQUIRED = False  # Email is required for signup (this should be inferred from SIGNUP_FIELDS)
#ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Options: 'username', 'email', or 'username_email'
# After signup, redirect to appointments page
#ACCOUNT_SIGNUP_REDIRECT_URL = '/appointments/'

ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}  # Use custom signup form
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username', 'password1*', 'password2*']  # Asterisk marks required fields
ACCOUNT_LOGIN_METHODS = {'email', 'username'}  # Use email for authentication

# Automatically log in users after signing up
#ACCOUNT_LOGIN_ON_SIGNUP = True

# Use only the email for login (implicitly handled by SIGNUP_FIELDS)
# Remove ACCOUNT_LOGIN_METHODS if unnecessary:
# ACCOUNT_LOGIN_METHODS = ['email']  # This can be removed, as 'email' is inferred from SIGNUP_FIELDS

# Configure Django Summernote

# Configure Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'silvol.urls'


TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'silvol.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

CSRF_TRUSTED_ORIGINS = [
    "https://silvol-3630ff49165c.herokuapp.com/",
    "https://silvol.herokuapp.com/",
]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Collects static files here
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Cloudinary Configuration
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.getenv('CLOUDINARY_URL')
}


# Media files (Images)
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
print("DEFAULT_FILE_STORAGE:", DEFAULT_FILE_STORAGE)



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
