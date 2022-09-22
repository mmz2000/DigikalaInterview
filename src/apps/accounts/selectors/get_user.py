from django.contrib.auth import get_user_model

User = get_user_model()


def get_user(**kwargs):
    return User.objects.get(**kwargs)
