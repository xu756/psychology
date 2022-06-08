import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-d^)^92dq$(*f^i8d+vc%)11s7eadb0-8fqywc#_%#ex$3j^x-!'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'chat',
    'channels',  # websockets
    'ckeditor',  # 这个

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'server.wsgi.application'
ASGI_APPLICATION = 'server.asgi.application'
DATABASES = {
    'default': {
        # mysql
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'psychology',
        'USER': 'xu',
        'PASSWORD': 'xjx756756',
        'HOST': '121.5.132.57',
        'PORT': '5700',
    }
}
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
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
USE_I18N = True

USE_L10N = True
MEDIA_URL = '/media/'  # 上传图片的路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 上传图片的根路径
CKEDITOR_UPLOAD_PATH = "ckeditor"
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')  # 指定样式收集目录
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    }
}
