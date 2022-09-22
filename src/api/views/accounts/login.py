from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.accounts.services import login
from src.errors import BadRequestException, ErrorEnum


class LoginAPIView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        data.setdefault("authenticator", "")
        data.setdefault("password", "")
        tokens = login(**data)
        if tokens is None:
            raise BadRequestException(
                message={"error": _("Invalid credentials")},
                error_type=[ErrorEnum.LoginAPIView.INVALID_CREDENTIALS],
            )
        response = {"ok": True, "data": tokens}
        return Response(response, status=status.HTTP_200_OK)
