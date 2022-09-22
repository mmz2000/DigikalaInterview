"""Common settings for django project."""

from os import environ
from os.path import abspath, dirname, join
from pathlib import Path
from sys import path


# GET ENV UTIL
def get_env(key, default=None, optinal=False):
    """Return environment variables with some options."""
    val = environ.get(key)
    if val is not None:
        return val
    elif default is not None:
        return default
    elif not optinal:
        raise ValueError(f"Environment variable {key} was not defined")


# END GET ENV UTIL


# PATH CONFIGURATION
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = dirname(dirname(abspath(__file__)))
PACKAGE_ROOT = dirname(PROJECT_ROOT)
# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(PACKAGE_ROOT)
# END PATH CONFIGURATION


# DEBUG CONFIGURATION
DEBUG = get_env("DEBUG", default="False") == "True"
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION

# APP CONFIGURATION
DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Admin panel and documentation:
    "django.contrib.admin",
    "django.contrib.admindocs",
)

THIRD_PARTY_APPS = ("rest_framework",)

# Apps specific for this project go here.
LOCAL_APPS = ("src.api", "src.apps.accounts")

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

# MIDDLEWARE CONFIGURATION
MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)
# END MIDDLEWARE CONFIGURATION

# URL CONFIGURATION
ROOT_URLCONF = "src.urls"
# END URL CONFIGURATION

# TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(PROJECT_ROOT, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# END TEMPLATE CONFIGURATION

# WSGI CONFIGURATION
WSGI_APPLICATION = "core.wsgi.application"
# END WSGI CONFIGURATION

# DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env("DEFAULT_DATABASE_NAME"),
        "USER": get_env("DEFAULT_DATABASE_USER"),
        "PASSWORD": get_env("DEFAULT_DATABASE_PASSWORD"),
        "HOST": get_env("DEFAULT_DATABASE_HOST"),
        "PORT": get_env("DEFAULT_DATABASE_PORT"),
    }
}
# END DATABASE CONFIGURATION

# Password validation CONFIGURATION
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# END Password validation CONFIGURATION

# GENERAL CONFIGURATION
LANGUAGE_CODE = get_env("LANGUAGE_CODE", default="en-us")

TIME_ZONE = get_env("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True
# END GENERAL CONFIGURATION

# MEDIA CONFIGURATION
MEDIA_ROOT = get_env("MEDIA_ROOT", default="media/")
MEDIA_URL = get_env("MEDIA_URL", default="media/")
# END MEDIA CONFIGURATION

# STATIC FILE CONFIGURATION
STATIC_ROOT = get_env("STATIC_ROOT", default="static/")
STATIC_URL = get_env("STATIC_URL", default="static/")
static_file_env = get_env("STATICFILES_DIRS", default="")
STATICFILES_DIRS = static_file_env.split(",")
# END STATIC FILE CONFIGURATION

# SECRET CONFIGURATION
SECRET_KEY = get_env("SECRET_KEY")
# END SECRET CONFIGURATION

# SITE CONFIGURATION
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS", default="*").split(",")
# END SITE CONFIGURATION


# LOGGING CONFIGURATION
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": get_env("DJANGO_LOG_LEVEL", default="INFO"),
            "propagate": False,
        },
    },
}
# END LOGGING CONFIGURATION

# DEFAULT_AUTO_FIELD CONFIGURATION
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# END DEFAULT_AUTO_FIELD CONFIGURATION

# CACHING CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": get_env("REDIS_URL"),
    }
}
# END CACHING CONFIGURATION

# RESTFARMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "src.api.exception_handler.api_exception_handler",
}
# END RESTFARMEWORK CONFIGURATION

# JWT CONFIGURATION
ACCESS_TTL = int(get_env("ACCESS_TTL"))
REFRESH_TTL = int(get_env("REFRESH_TTL"))
JWT_SECRET = get_env("JWT_SECRET")
if (
    len(JWT_SECRET.encode("utf-8")) < 64
    or len(JWT_SECRET.encode("utf-8")) > 128
):
    raise ValueError("JWT_SECRET must be between 64 and 128 bytes")
# END JWT CONFIGURATION
