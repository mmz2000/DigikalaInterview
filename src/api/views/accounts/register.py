from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.accounts.services import register_user


class RegisterAPIView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        register_data = register_user(data)
        response = {"ok": True, "data": register_data}
        return Response(response, status=status.HTTP_201_CREATED)
