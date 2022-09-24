from django.urls import include, path

from src.api.urls.accounts import urlpatterns as accounts_urls
from src.api.urls.feed import urlpatterns as feed_urls

urlpatterns = [
    path("accounts/", include(accounts_urls)),
    path("feed/", include(feed_urls)),
]
