from django.db import transaction

from src.apps.accounts.functions import login
from src.apps.accounts.serializers import CreateUserSerializer
from src.errors import BadRequestException, SerializerErrors


@transaction.atomic
def register_user(data):
    serializer = CreateUserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        data = login(user)
        data.update(serializer.data)
        return data
    errors = serializer.errors
    error_enum = [
        SerializerErrors.create_user_serialzier.get(key) for key in errors
    ]
    raise BadRequestException(message=errors, error_type=error_enum)
