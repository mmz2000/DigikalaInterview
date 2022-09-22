from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers

from src.utils import validate_password


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "first_name", "last_name")
        extra_kwargs = {
            "username": {"required": True},
            "email": {"required": True},
            "password": {"write_only": True, "required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError(_("Password is required"))
        if not validate_password(value):
            raise serializers.ValidationError(
                "{}/n{}/n{}/n{}/n{}/n{}/n{}".format(
                    _("Password is invalid."),
                    _("hint:"),
                    _("it must contain at least eight number,"),
                    _("it must contain at least one uppercase alphabet,"),
                    _("it must contain at least one lowercase alphabet,"),
                    _("it must contain at least one special character."),
                    _("it must not be too common :D"),
                )
            )
        return value
