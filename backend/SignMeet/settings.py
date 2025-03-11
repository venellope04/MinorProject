import os
from pathlib import Path

# Define the base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Generate your SECRET_KEY (replace 'your-secret-key' with the generated key)
SECRET_KEY = 'Yl9ttWcun4XCemOEOCi5FeGCXNXPtu7Ct_3gqM3JIav_Xe7Us6ZsyH-oVlr46pHYWNk'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'conferencing',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'SignMeet.urls'

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
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                #'rest_framework.templatetags.rest_framework',
            ],
        },
    },
]

WSGI_APPLICATION = 'SignMeet.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),  # Convert Path to string
    }
}

# Channels configuration
ASGI_APPLICATION = 'SignMeet.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6380)],  # Update the port to 6380
        },
    },
}




# Allowed hosts for development
DEBUG = True
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)


# Ensure the directory is included in STATICFILES_DIRS
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "backend" / "conferencing" / "static",
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
] # Replace with your frontend's URL

# settings.py

# Agora credentials
AGORA_APP_ID = '71fbf1e2263a49869725faa8404523ec'
AGORA_API_KEY = 'd8d112b189d749a0b283708e3eb53667'
AGORA_API_SECRET = '8796d7f317ff421c8080ace9c1e432f2'

