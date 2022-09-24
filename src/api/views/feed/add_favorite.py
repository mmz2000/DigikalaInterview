from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.feed.services import add_favorite_feed
from src.errors import ErrorEnum, ModelNotFoundException, NotFoundException


class AddToFavoriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        feed_id = kwargs.get("feed_id")
        try:
            add_favorite_feed(self.request.user.id, feed_id)
        except ModelNotFoundException:
            raise NotFoundException(
                message={"feed_id": _("feed with this id doesn't exists")},
                error_type=[ErrorEnum.AddToFavoriteAPIView.FEED_NOT_FOUND],
            )
        response = {"ok": True, "data": None}
        return Response(response, status=status.HTTP_201_CREATED)
