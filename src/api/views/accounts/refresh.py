from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.accounts.services import refresh
from src.errors import BadRequestException, ErrorEnum, InvalidRefresh


class RefreshAPIView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        refresh_token = data.get("refresh_token")
        if refresh_token is None:
            raise BadRequestException(
                message={"refresh_token": _("refresh token must be provided")},
                error_type=[ErrorEnum.RefreshAPIView.EMPTY_REFRESH],
            )
        try:
            tokens = refresh(refresh_token)
        except InvalidRefresh:
            raise BadRequestException(
                message={"refresh_token": _("Invalid refresh token")},
                error_type=[ErrorEnum.RefreshAPIView.INVALID_REFRESH_TOKEN],
            )
        response = {"ok": True, "data": tokens}
        return Response(response, status=status.HTTP_200_OK)
