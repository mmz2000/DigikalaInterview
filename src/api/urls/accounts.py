from django.urls import path

from src.api.views.accounts import RegisterAPIView

urlpatterns = [
    path("sign-up/", RegisterAPIView.as_view(), name="register"),
]
