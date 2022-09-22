from django.urls import include, path

from src.api.urls.accounts import urlpatterns as accounts_urls

urlpatterns = [
    path("accounts/", include(accounts_urls)),
]
