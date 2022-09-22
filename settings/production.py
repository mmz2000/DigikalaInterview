"""Production settings for django project."""
from os import environ

from django.core.exceptions import ImproperlyConfigured

from settings.common import *

# PRODUCTION APPS CONFIGURATION
INSTALLED_APPS = ("corsheaders",) + INSTALLED_APPS + ("gunicorn",)
# PRODUCTION APPS CONFIGURATION

# EMAIL CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = get_env("EMAIL_HOST", optinal=True)
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD", optinal=True)
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER", optinal=True)
EMAIL_PORT = get_env("EMAIL_PORT", optinal=True)
EMAIL_SUBJECT_PREFIX = "[{}] ".format(SITE_NAME)
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION


# CORSHEADERS CONFIGURATION
CSRF_TRUSTED_ORIGINS = get_env("CSRF_TRUSTED_ORIGINS", default="").split(",")
CSRF_COOKIE_DOMAIN = get_env("CSRF_COOKIE_DOMAIN", optinal=True)
CORS_ORIGIN_REGEX_WHITELIST = [r".*"]  # TODO fill this
CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
MIDDLEWARE += ("corsheaders.middleware.CorsMiddleware",)
CORS_URLS_REGEX = r".*"  # TODO fill this
# END CORSHEADERS CONFIGURATION
DEBUG = get_env("DEBUG") == "True"
