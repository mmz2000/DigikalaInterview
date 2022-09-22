from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers

from src.utils import validate_password


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        if not validate_password(value):
            raise serializers.ValidationError(
                "{}/n{}/n{}/n{}/n{}".format(
                    _("Password is invalid."),
                    _("hint:"),
                    _("it must contain at least eight number,"),
                    _("it must contain at least one uppercase alphabet,"),
                    _("it must contain at least one lowercase alphabet,"),
                )
            )
        return value
