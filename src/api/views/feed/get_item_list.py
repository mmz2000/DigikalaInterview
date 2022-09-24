from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.feed.services import get_limited_item_list
from src.errors import BadRequestException, ErrorEnum, NotFoundException


class GetItemListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user_id = self.request.user.id
        try:
            limit = int(self.request.query_params.get("limit", 10))
            offset = int(self.request.query_params.get("offset", 0))
        except ValueError:
            raise BadRequestException(
                message={
                    "error": _("invlid limit or offset"),
                },
                error_type=[
                    ErrorEnum.GetItemListAPIView.INVALID_LIMIT_OR_OFFSET
                ],
            )
        if limit < 1 or offset < 0:
            raise BadRequestException(
                message={
                    "error": _("invlid limit or offset"),
                },
                error_type=[
                    ErrorEnum.GetItemListAPIView.INVALID_LIMIT_OR_OFFSET
                ],
            )
        data, count = get_limited_item_list(
            user_id=user_id, limit=limit, offset=offset
        )
        if len(data) == 0:
            raise NotFoundException(
                message={"error": _("no items found")},
                error_type=[
                    ErrorEnum.GetItemListAPIView.INVALID_LIMIT_OR_OFFSET
                ],
            )
        response = {"ok": True, "data": {"items": data, "count": count}}
        return Response(response, status=status.HTTP_200_OK)
