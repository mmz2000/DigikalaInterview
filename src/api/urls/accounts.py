from django.urls import path

from src.api.views.accounts import (
    LoginAPIView,
    RefreshAPIView,
    RegisterAPIView,
)

urlpatterns = [
    path("sign-up/", RegisterAPIView.as_view(), name="register"),
    path("sign-in/", LoginAPIView.as_view(), name="login"),
    path("refresh/", RefreshAPIView.as_view(), name="refresh"),
]
