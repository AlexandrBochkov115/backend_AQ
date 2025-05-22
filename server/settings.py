from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Рассмотрите использование переменных окружения для секретного ключа
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-!1bjdp6^8lt+(fmk%w^)=jj9r(22s9$!6*_-@g-=9+m76-!tsd')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # В продакшне всегда должно быть False

# Настройки для защиты от XSS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Настройки HTTPS (активируются в продакшне)
SESSION_COOKIE_SECURE = False  # Поставьте True при использовании HTTPS
CSRF_COOKIE_SECURE = False    # Поставьте True при использовании HTTPS
SECURE_SSL_REDIRECT = False   # Поставьте True при использовании HTTPS

# Список доверенных хостов для защиты от подделки заголовков Host
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    # Добавьте ваши домены для продакшна
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pools',
    'terms',
    'project',
    'catalog',
    'django_filters',
    'drf_yasg',
    'contact',
    'corsheaders',
]

# Защита от SQL-инъекций через параметризованные запросы
# Django ORM по умолчанию использует параметризованные запросы,
# но важно избегать raw SQL и особенно не доверять пользовательскому вводу

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Отключаем Browsable API в продакшне
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',  # Разрешаем только JSON
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Защита от clickjacking
    'django.middleware.security.SecurityMiddleware',  # Дополнительные заголовки безопасности
]

# Настройки CORS - будьте осторожны в продакшне
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://localhost:3000",  # для HTTPS
]
CORS_ALLOW_ALL_ORIGINS = False  # В продакшне должно быть False

ROOT_URLCONF = 'server.urls'

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
            # Автоматическое экранирование для защиты от XSS
            'autoescape': True,
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

# Database
# Используйте параметризованные запросы для защиты от SQL-инъекций
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aquadreams',
        'USER': 'django_user',
        'PASSWORD': '123456',  # Рассмотрите использование переменных окружения
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # Строгий режим MySQL
            'charset': 'utf8mb4',
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,  # Рекомендуется минимум 12 символов
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Дополнительные заголовки безопасности
SECURE_HSTS_SECONDS = 31536000  # 1 год - только для HTTPS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Логирование SQL-запросов (только для разработки)
if DEBUG:
    LOGGING = {
        'version': 1,
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            }
        }
    }