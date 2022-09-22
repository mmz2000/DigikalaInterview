from django.contrib.auth import get_user_model
from rest_framework import authentication

from src.apps.accounts.functions import claim_token, validate_token

User = get_user_model()


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        access_from_cookie = request.COOKIES.get(
            "HTTP_ACCESS"
        ) or request.COOKIES.get("HTTP_AUTHORIZATION")
        access_from_header = request.META.get(
            "HTTP_ACCESS"
        ) or request.META.get("HTTP_AUTHORIZATION")
        access = access_from_cookie or access_from_header
        if access is None:
            return None
        if access[0:7] == "Bearer ":
            access = access[7:]
        if not validate_token(access):
            return None
        token_data = claim_token(token=access)
        if token_data.get("type") != "access":
            return None
        user_id = token_data.get("user_id")
        user = User.objects.get(id=user_id)
        return (user, None)
