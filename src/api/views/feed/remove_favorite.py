from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.feed.services import remove_favorite_feed
from src.errors import ErrorEnum, ModelNotFoundException, NotFoundException


class RemoveFromFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, *args, **kwargs):
        feed_id = kwargs.get("feed_id")
        try:
            remove_favorite_feed(self.request.user.id, feed_id)
        except ModelNotFoundException:
            raise NotFoundException(
                message={"feed_id": _("feed with this id doesn't exists")},
                error_type=[
                    ErrorEnum.RemoveFromFavoriteAPIView.FEED_NOT_FOUND
                ],
            )
        response = {"ok": True, "data": None}
        return Response(response, status=status.HTTP_200_OK)
