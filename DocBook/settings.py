import os
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+7d1fysjucid6p0v=u8a%q++_6s-)75pbhv0icu-c@0@$3$69q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['docbook-backend.herokuapp.com', '127.0.0.1', 'localhost',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hospital',
    'rest_framework',
    'django_extensions',
    'cloudinary_storage',
    'drf_yasg',
    'corsheaders',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'hospital.backends.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'DocBook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DocBook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000000

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

AUTH_USER_MODEL = "hospital.User"


MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
# JWT_AUTH = {
#     'JWT_RESPONSE_PAYLOAD_HANDLER': 'hospital.utils.my_jwt_response_handler'
# }
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'hospital.backends.JWTAuthentication'
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#
#     ),
# }

JWT_SECRET_KEY = 'qwerty12345678912345678'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'difsz7dn1',
    'API_KEY': '411511293197637',
    'API_SECRET': 'dNsaFseOYgj_y8xOT1P_8Rayo40'
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [

'http://localhost:3000',
'http://docbookk.herokuapp.com',
]
CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]
CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
]


# STRIPE_PUBLIC_KEY = 'pk_test_51HlGPMEwvqnTnN1jIhCuqAkYruAvLnd5RkP2DHRq6k8wJwoYVPDJpSpIiOLAMw1gEdzN7c1WpHP6P5WB82KmhCSg009VGXHMDW'
# STRIPE_PRIVATE_KEY = 'sk_test_51HlGPMEwvqnTnN1jmLixtF5asItUIw99IVugVj1FBPUchdkOzJG69qjtQHZhPvQgErd9d8T570QzN1dbjpW7b2Nd00gK4ot95e'