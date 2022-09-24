from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.feed.services import get_feed_list


class GetFeedListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        response = {"ok": True, "data": get_feed_list(self.request.user.id)}
        return Response(response, status=status.HTTP_200_OK)
